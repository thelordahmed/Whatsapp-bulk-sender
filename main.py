import csv
import random
from time import sleep
from model import Model
from PySide2 import QtWidgets, QtCore
from view import View
from whatsapp import WhatsApp
from threading import Thread
from ast import literal_eval
from features_controller import country_code



class Signals(QtCore.QObject):
    start_btn = QtCore.Signal()


class Main:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.wa = WhatsApp()
        self.status = {
            "sent": "Message Sent!",
            "no whatsapp": "Number is not found on whatsapp",
        }
        # Continue last sending session confirmation
        if len(self.model.getAllRecords()) != 0:
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

        ###############################################
        ######## Connections ##########################
        self.view.start_btn.clicked.connect(self.start_process)
        self.view.sheet_btn.clicked.connect(self.view.openFileDialog)
        self.view.attachments_btn.clicked.connect(self.view.getImagePath)
        self.view.pushButton.clicked.connect(self.view.appendToPlainTextBox)
        self.view.stop_btn.clicked.connect(self.view.changeStateToStopped)
        self.view.commandLinkButton.clicked.connect(self.view.copyrights)
        self.view.newsession_btn.clicked.connect(self.newSessionFunc)
        self.view.csv_btn.clicked.connect(self.export_func)
        self.view.multi_messages_btn.clicked.connect(self.view.openMultiFileDialog)
        ###############################################

    def newSessionFunc(self):
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
            return None
        else:
            data_list = model2.getDataFromSheet(self.view.sheet_le.text())

        # disabling start button and activating stop button
        self.view.startbtn_process()
        self.view.statusbar.showMessage(f"   >> Opening WhatsApp Web... <<")

        # handling browser error
        try:
            self.wa.open()
        except Exception as e:
            print(e)
            self.view.state = "error"
            self.view.stopbtn_process()
            self.view.statusbar.showMessage(
                "There's something wrong with Chrome browser .. please try updating google chrome")

        # switching to report panel
        self.view.listWidget.setCurrentRow(1)

        messages_sent = 0

        for contact in data_list:
            try:  # handeler for unknown errors
                if self.view.state == "stopped":
                    break
                if int(self.view.messages_sbox.text()) == messages_sent:
                    mins = self.view.minutes_sbox.text()
                    self.view.statusbar.showMessage(f"   >> Reached the Sending Limit .. waiting for {mins} mins <<")
                    sleep(int(self.view.minutes_sbox.text()) * 60)
                    messages_sent = 0
                name = contact[0]
                if country_code is not None:
                    phone = contact[2] + contact[1]
                else:
                    phone = contact[1]
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
                    theMessage = random.choice(multi_messages)
                else:
                    theMessage = messageFromTextBox
                isUnsavedChecked = self.view.checkBox.isChecked()

                if self.wa.number_search(phone) is False:
                    if self.connectionLoop(phone) == "search is already false":
                        if self.view.state == "stopped":
                            break
                        if isUnsavedChecked is True:  # if checked - call unsaved sending
                            if self.wa.unsaved_number_search(phone) is False:
                                if self.connectionLoop(phone, "unsaved") == "search is already false":
                                    self.skipToNextNumber(name, phone, "no whatsapp", model2)
                                    self.view.statusbar.showMessage(f"   >> Number is not found on whatsapp! <<")
                                    continue
                        else:
                            self.skipToNextNumber(name, phone, "no whatsapp", model2)
                            self.view.statusbar.showMessage(f"   >> Number is not found on whatsapp! <<")
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
                    self.wa.sending_image(attachments_paths_list)
                # checking if one line message checked or same format
                if self.view.oneline_rb.isChecked() is True:
                    self.wa.sending(theMessage, "{name}", name)
                else:
                    self.wa.sending_sameFormat(theMessage, "{name}", name)

                if contact_card != "":
                    self.wa.sending_contact(contact_card)
                messages_sent += 1

                self.view.statusbar.showMessage(f"   >> Message Sent Successfully! <<")
                self.skipToNextNumber(name, phone, "sent", model2)
            except Exception as e:
                self.view.state = "error"
                print(e)
                break

        # -------------------- Finished behaviour ------------------------
        if self.view.state == "stopped":
            self.view.stopbtn_process()
            self.view.statusbar.showMessage(f"   >> Stopped! <<")
        elif self.view.state == "error":
            self.view.stopbtn_process()
            self.view.statusbar.showMessage(f"   >> something wrong happened.. please restart the bot and try again!<<")
        else:
            self.view.statusbar.showMessage(f"   >> Sending Session Completed Successfully! <<")
            self.view.stopbtn_process()
            self.view.state = "stopped"
        # ---------------------------------------------------------------

    def getMultiMessages(self, paths):
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


###########################################################


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = Main()
    app.exec_()