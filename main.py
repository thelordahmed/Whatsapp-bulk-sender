import csv
import os
import platform
import random
import shutil
import subprocess
from time import sleep
from model import Model
from PySide2 import QtWidgets, QtCore
from view import View
from whatsapp import WhatsApp
from threading import Thread
from ast import literal_eval
from features_controller import country_code, extra_var, copyright_link, language
from license_validation import License
import sys
import traceback


if platform.system() == "Darwin":
    data_folder = f"{os.path.expanduser('~')}/Library/WhatsappSenderData/Data"
else:
    data_folder = "Data"


class Signals(QtCore.QObject):
    start_btn = QtCore.Signal()
    error_message = QtCore.Signal(str, str)



class Main:
    def __init__(self):
        self.sig = Signals()
        self.api_url = "https://softwarekeys.herokuapp.com"
        self.language = language
        if platform.system() == "Darwin":
            os.system("mkdir ~/Library/WhatsappSenderData")
            os.system("mkdir ~/Library/WhatsappSenderData/Data")
        else:
            os.system("mkdir Data")
        self.model = Model()
        self.view = View(self.api_url)
        self.view.adjustSize()
        self.license = License(self.api_url, self.view)
        # Sending Key Request if pre-saved key found
        try:
            if platform.system() == "Darwin":
                with open(os.path.join(data_folder, "license_key.txt"), "r") as f:
                    key = f.read()
            else:
                with open(os.path.join(r"C:\ProgramData", "license_key.txt"), "r") as f:
                    key = f.read()
            self.license.validate(key)
        except FileNotFoundError:
            pass
        self.wa = WhatsApp()
        if self.language == "italian":
            self.status = {
                "sent": "Messaggio inviato!",
                "no whatsapp": "Numero non trovato su whatsapp",
            }
        else:
            self.status = {
                "sent": "Message Sent!",
                "no whatsapp": "Number is not found on whatsapp",
            }
        # Continue last sending session confirmation
        if len(self.model.getAllRecords()) != 0:
            if self.language == "italian":
                res = self.view.confirmMessage("Continuare l'ultima sessione?",
                                               "Vuoi continuare l'ultima sessione di invio?")
            else:
                res = self.view.confirmMessage("Continue last session?",
                                               "Do you want to Continue the last sending session?")
            if res is True:
                values = self.model.getInterfaceValues()
                self.view.loadInterfaceValues(values)
                data = self.model.getAllRecords()
                for record in data:
                    self.view.addToTableWidget(record)
            else:
                self.model.clearDatabase()

        # check to disable or enable logout btn
        if os.path.exists(self.wa.browserAuthDirectory) is False:
            self.view.logout_btn.setDisabled(True)

        ###############################################
        ######## Connections ##########################
        self.view.start_btn.clicked.connect(self.start_process)
        self.view.sheet_btn.clicked.connect(self.view.openFileDialog)
        self.view.attachments_btn.clicked.connect(self.view.getImagePath)
        self.view.pushButton.clicked.connect(self.view.appendToPlainTextBox)
        self.view.stop_btn.clicked.connect(self.view.changeStateToStopped)
        self.view.append_newmessage.clicked.connect(self.view.appendToPlainTextBox_newmessage)
        if copyright_link is True:
            self.view.commandLinkButton.clicked.connect(self.view.copyrights)
        self.view.newsession_btn.clicked.connect(self.newSessionFunc)
        self.view.csv_btn.clicked.connect(self.export_func)
        self.view.multi_messages_btn.clicked.connect(self.view.openMultiFileDialog)
        if extra_var is not None:
            self.view.extra_var_btn.clicked.connect(self.view.appendToPlainTextBox_extraVar)
        self.view.logout_btn.clicked.connect(self.logout_btn_func)
        self.view.contact_groupbox.toggled.connect(lambda: self.view.contactCard_le.setStyleSheet("color:white"))
        self.sig.error_message.connect(self.view.error_message)
        ###############################################

    def newSessionFunc(self):
        if self.language == "italian":
            res = self.view.confirmMessage("cancellare i dati della sessione corrente?", "Vuoi iniziare una nuova sessione?")

        else:
            res = self.view.confirmMessage("clear current session data?", "Do you want to start a new session?")
        if res is True:
            self.model.clearDatabase()
            self.view.tableWidget.setRowCount(0)

    ###############################################
    ######## SLOTS ################################
    def start_process(self):
        self.view.state = "started"
        Thread(target=self.process).start()

    def export_func(self):
        try:
            path = self.view.saveDialog()
            data = self.model.getAllRecords()
            with open(path, "w", encoding = "utf-8", newline = "") as f:
                for row in data:
                    writer = csv.writer(f)
                    writer.writerow(row)
        except FileNotFoundError:
            print("saving cancelled!")

    ###############################################

    def logout_btn_func(self):
        self.wa.logout_btn()
        self.view.logout_btn.setDisabled(True)

    @staticmethod
    def getMultiMessages(paths):
        """
        :param paths: list of paths string
        :return: list of messages
        """
        messages = []
        for path in paths:
            with open(path, encoding="utf-8") as f:
                message = f.read()
            messages.append(message)
        return messages


    def connectionLoop(self, phone, unsavedOrNormal="normal"):
        if self.wa.connectionCheck() is False:
            while self.wa.connectionCheck() is False and self.view.state == "started":
                if self.language == "italian":
                    self.view.statusbar.showMessage("   **** Connessione persa .. tentativo di connessione in 5 secondi ****", 3)
                else:
                    self.view.statusbar.showMessage("   **** Connection Lost .. trying to connect in 5 seconds ****", 3)
                sleep(5)
            # when connection is back - try to search the same number again
            if unsavedOrNormal == "nomral":
                if self.wa.number_search(phone) is False:
                    return "search is already false"
                else:
                    return "number found"
            else:
                if self.wa.unsaved_number_search(phone) is False:
                    return "search is already false"
                else:
                    return "number found"
        else:
            return "search is already false"

    def skipToNextNumber(self, name, phone, status, modelObj):
        modelObj.addTodata((name, phone, self.status[status]))
        self.view.addToTableWidget((name, phone, self.status[status]))

    def sending_code(self, message, attachments_paths):
        if "{new message}" in message:
            messages = message.split("{new message}")
        else:
            messages = [message]
        if attachments_paths is not None:
            if self.view.textCaption_rb.isChecked() is True:
                # sending the first message only as caption (that's what most clients need!)
                self.wa.sending_image_with_caption(attachments_paths, messages[0].strip())
                if len(messages) > 1:
                    for i in messages[1:]:
                        self.wa.sending_sameFormat(i.strip())
            else:
                for i in messages:
                    self.wa.sending_sameFormat(i.strip())
                self.wa.sending_image(attachments_paths)
        else:
            for i in messages:
                self.wa.sending_sameFormat(i.strip())

    @staticmethod
    def process_exists(process_name):
        """
        usefull method to check on current running task
        """
        call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
        # use buildin check_output right away
        output = subprocess.check_output(call).decode()
        # check in last line for process name
        last_line = output.strip().split('\r\n')[-1]
        # because Fail message could be translated
        return last_line.lower().startswith(process_name.lower())



    def process(self):
        model2 = Model()

        # --------------- saving the interface values ---------------
        if self.view.checkBox.isChecked() is True:
            checkbox_intValue = 1
        else:
            checkbox_intValue = 0

        interface_data = (
            self.view.sheet_le.text(),
            self.view.messages_sbox.text(),
            self.view.minutes_sbox.text(),
            checkbox_intValue,
            self.view.attachments_le.text(),
            self.view.message_text.toPlainText(),
            self.view.contactCard_le.text()
        )

        model2.saveInterfaceValues(interface_data)
        # ---------------------------------------------------------------

        # check if sheet path found in the interface - if False -> app will not start
        if self.view.sheet_le.text() is "":
            self.sig.error_message.emit("error", "Contacts Sheet Not Found!")
            return None
        else:
            try:
                data_list = model2.getDataFromSheet(self.view.sheet_le.text())
            except Exception as e:
                self.sig.error_message.emit("Error", f"Sheet Formation is not correct!\nError:\n{e}\nTraceback:\n{traceback.extract_tb(e.__traceback__)}")
                return False

        # disabling start button and activating stop button
        self.view.startbtn_process()
        if self.language == "italian":
            self.view.statusbar.showMessage(f"   >> Apertura di WhatsApp Web... <<")
        else:
            self.view.statusbar.showMessage(f"   >> Opening WhatsApp Web... <<")

        # handling browser error
        try:
            if self.view.chrome_rb.isChecked():
                self.wa.open("chrome")
            else:
                self.wa.open("firefox")
        except Exception as e:
            self.sig.error_message.emit("Error", f"There's an Error with the browser!\nError:\n{e}\nTraceback:\n{traceback.extract_tb(e.__traceback__)}")
            self.view.state = "error"
            self.view.stopbtn_process()
            if self.language == "italian":
                self.view.statusbar.showMessage(
                    "C'è qualcosa di sbagliato nel browser Chrome .. prova ad aggiornare Google Chrome")
            else:
                self.view.statusbar.showMessage(
                    "There's something wrong with Chrome browser .. please try updating google chrome")
            return False
        # PASSING THE WINDOW OBJECT TO VIEW TO CLOSE CHROME DIRVER WINDOW ON CLOSE EVENT
        self.view.whatsapp_window_obj = self.wa.get_window_object()
        # # SAVING PRFILE DIR IN FIREFOX
        # if not self.view.chrome_rb.isChecked():
        #     currentProfilePath = self.wa._window.capabilities["moz:profile"]
        #     profileStoragePath = os.path.join(data_folder, "firefoxProfile")
        #     shutil.copytree(currentProfilePath, profileStoragePath,
        #                     ignore_dangling_symlinks=True)

        # switching to report panel
        self.view.listWidget.setCurrentRow(1)

        messages_sent = 0

        for contact in data_list:
            if self.view.time_groupBox.isChecked() is True:
                # start and end time check ------------
                start_time = self.view.from_time.time().toPython()
                end_time = self.view.to_time.time().toPython()
                startTime_return = self.wa.startTime_check(start_time)
                endTime_return = self.wa.endTime_check(end_time, start_time)
                if startTime_return is not True:
                    if self.language == "italian":
                        self.view.statusbar.showMessage(
                            f"  ==>>  In attesa ... inizierà l'invio alle {start_time.strftime('%I:%M %p')} <<==  ")
                    else:
                        self.view.statusbar.showMessage(f"  ==>>  Waiting... will start sending at {start_time.strftime('%I:%M %p')} <<==  ")
                    self.view.stop_btn.setDisabled(True)
                    sleep(startTime_return)
                    self.view.stop_btn.setEnabled(True)
                if endTime_return is not True:
                    self.view.stop_btn.setDisabled(True)
                    if self.language == "italian":
                        self.view.statusbar.showMessage(f"  ==>>  In attesa ... inizierà l'invio domani alle {start_time.strftime('%I:%M %p')} <<==  ")
                    else:
                        self.view.statusbar.showMessage(f"  ==>>  Waiting... will start sending tomorrow at {start_time.strftime('%I:%M %p')} <<==  ")
                    sleep(endTime_return)
                    self.view.stop_btn.setEnabled(True)
                # ---------------------------------------
            try:  # handeler for unknown errors
                if self.view.state == "stopped":
                    break
                if int(self.view.messages_sbox.text()) == messages_sent:
                    mins = self.view.minutes_sbox.text()
                    if self.language == "italian":
                        self.view.statusbar.showMessage(f"   >> Raggiunto il limite di invio ... in attesa di {mins} minuti <<")

                    else:
                        self.view.statusbar.showMessage(f"   >> Reached the Sending Limit .. waiting for {mins} mins <<")
                    sleep(int(self.view.minutes_sbox.text()) * 60)
                    messages_sent = 0
                name = contact[0]
                if country_code is not None:
                    phone = contact[2] + contact[1]
                else:
                    phone = contact[1]

                # extra variable check
                if extra_var is not None and country_code is not None:
                    extra_variable = contact[3]
                elif extra_var is not None and country_code is None:
                    extra_variable = contact[2]
                else:
                    extra_variable = ""
                if self.language == "italian":
                    self.view.statusbar.showMessage(f"   >> Invio a {name} <<")
                else:
                    self.view.statusbar.showMessage(f"   >> Sending to {name} <<")
                if model2.findContact(phone) is not None:
                    continue  # skip if number found in the database
                attachments_paths_string = self.view.attachments_le.text()
                contact_card = self.view.contactCard_le.text()
                messageFromTextBox = self.view.message_text.toPlainText()
                # checking if there are multi messages choosed
                paths_string = self.view.multi_messages_le.text()
                if paths_string != "":
                    paths = literal_eval(paths_string)  # converting the paths string to real list
                    multi_messages = self.getMultiMessages(paths)
                    multi_messages.append(messageFromTextBox)   # adding the view message to the list
                    theMessage = random.choice(multi_messages).replace("{name}", name).replace("{variable}", extra_variable)
                else:
                    theMessage = messageFromTextBox.replace("{name}", name).replace("{variable}", extra_variable)
                isUnsavedChecked = self.view.checkBox.isChecked()

                if self.wa.number_search(phone) is False:
                    if self.connectionLoop(phone) == "search is already false":
                        if self.view.state == "stopped":
                            break
                        if isUnsavedChecked is True:  # if checked - call unsaved sending
                            if self.wa.unsaved_number_search(phone) is False:
                                if self.connectionLoop(phone, "unsaved") == "search is already false":
                                    self.skipToNextNumber(name, phone, "no whatsapp", model2)
                                    continue
                        else:
                            self.skipToNextNumber(name, phone, "no whatsapp", model2)
                            continue
                    else:
                        pass
                if self.view.state == "stopped":
                    break

                #########
                # Sending
                #########
                if attachments_paths_string != "":
                    attachments_paths_list = literal_eval(attachments_paths_string)
                else:
                    attachments_paths_list = None

                self.sending_code(theMessage, attachments_paths_list)
                # CONTACT CARD
                if self.view.contact_groupbox.isChecked():
                    if "," in contact_card:
                        numbers = contact_card.split(",")
                        for num in numbers:
                            self.wa.sending_contact(num)
                    else:
                        self.wa.sending_contact(contact_card)
                messages_sent += 1

                self.skipToNextNumber(name, phone, "sent", model2)
            except Exception as e:
                self.view.state = "error"
                self.sig.error_message.emit("Error", f"Something Wrong Happened\nError:\n{e}\nTraceback:\n{traceback.extract_tb(e.__traceback__)}")
                print(e)
                break


        # Custom functionlity
        # -------- sleep 24 hours then clear the data base and resend all messages -----------
        if self.view.repeat_sending.isChecked() is True and self.view.state != "stopped":
            if self.language == "italian":
                self.view.statusbar.showMessage(f"   >> Completato, inizierà a inviare di nuovo tra 24 ore! <<")
            else:
                self.view.statusbar.showMessage(f"   >> Completed, will start sending again in 24 hours! <<")
            sleep(86400)
            model2.clearDatabase()
            self.view.tableWidget.setRowCount(0)
            self.process()  # Recursive function



        # -------------------- Finished behaviour ------------------------
        if self.view.state == "stopped":
            self.view.stopbtn_process()
            if self.language == "italian":
                self.view.statusbar.showMessage(f"   >> Fermato! <<")
            else:
                self.view.statusbar.showMessage(f"   >> Stopped! <<")
        elif self.view.state == "error":
            self.view.stopbtn_process()
            if self.language == "italian":
                self.view.statusbar.showMessage(f"   >> è successo qualcosa di sbagliato .. riavvia il bot e riprova!! <<")

            else:
                self.view.statusbar.showMessage(
                    f"   >> something wrong happened.. please restart the bot and try again!<<")
        else:
            if self.language == "italian":
                self.view.statusbar.showMessage(f"   >> Invio della sessione completato con successo! <<")
            else:
                self.view.statusbar.showMessage(f"   >> Sending Session Completed Successfully! <<")
            self.view.stopbtn_process()
            self.view.state = "stopped"
        # ---------------------------------------------------------------



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = Main()
    app.exec_()
