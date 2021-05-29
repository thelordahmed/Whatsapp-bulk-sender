from PySide2 import QtCore, QtGui
from PySide2.QtGui import QCloseEvent, QTextOption, Qt
from PySide2.QtWidgets import *
from webbrowser import open
# Import your design class
from design import Ui_MainWindow as design
import features_controller


class View(QMainWindow, design):
    def __init__(self, api_url,parent=None):
        super(View, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.show()
        self.api_url = api_url
        self.setWindowTitle(f"WhatsApp Bulk Sender {features_controller.version}")
        self.stop_btn.setDisabled(True)
        self.whatsapp_window_obj = None
        # hidding all to validate license first
        self.main_frame.hide()
        self.buttons_frame.hide()
        self.logout_btn.hide()
        self.license_frame.show()
        self.commandLinkButton.setText(f"Copyright © 2020 {features_controller.copyright_text}")
        # TODO - add a label about those shorcuts to the interface
        # --- shortcuts START
        self.shortcutR = QShortcut(
            QtGui.QKeySequence('Ctrl+r'), self.message_text)
        self.shortcutL = QShortcut(
            QtGui.QKeySequence('Ctrl+l'), self.message_text)
        self.shortcutR.activated.connect(lambda: self.message_text.document().setDefaultTextOption(QTextOption(Qt.AlignRight)))
        self.shortcutL.activated.connect(lambda: self.message_text.document().setDefaultTextOption(QTextOption(Qt.AlignLeft)))
        # --- shortcuts END
        self.state = "stopped"
        if features_controller.repeat_every_24h is False:
            self.repeat_sending.setDisabled(True)
            self.repeat_sending.setStyleSheet("color:grey")



        if features_controller.contact_card_enabled is False:
            self.contact_groupbox.setDisabled(True)

        if features_controller.attachments_enabled is False:
            self.groupBox_3.setDisabled(True)

        if features_controller.multi_messages_enabled is False:
            self.multi_messages_btn.setDisabled(True)

        if features_controller.show_columns_note is False:
            self.textBrowser.hide()

        if features_controller.scheduled_sending is False:
            self.listWidget.item(2).setFlags(QtCore.Qt.NoItemFlags)

######################################
######### SLOTS ######################
    
    def startbtn_process(self):
        self.state = "started"
        self.start_btn.setDisabled(True)
        self.stop_btn.setEnabled(True)

    def stopbtn_process(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setDisabled(True)

    def copyrights(self):
        if features_controller.copyright_url is not None:
            open(features_controller.copyright_url)
    ######################################

    # Customizing the close event
    def closeEvent(self, event: QCloseEvent):
        self.whatsapp_window_obj.quit()
        # if self.chrome_rb.isChecked():
        #     if platform.system() == "Darwin":
        #         os.system("killall chromedriver")
        #         os.system("killall 'Google Chrome'")
        #     else:
        #         os.system("taskkill /t /F /im chromedriver.exe")
        #     # requests.put(f"{self.api_url}/connected/decrease")
        # else:
        #     if platform.system() == "Darwin":
        #         os.system('pkill -f firefox')
        #     else:
        #         os.system("taskkill /t /F /im firefox.exe")
        #     # requests.put(f"{self.api_url}/connected/decrease")


    def addToTableWidget(self, data):  # slot >> trigger singal
        """
        Use this method if you have TableWidget to add items in rows
        :param data: tuple of values (1, 2, 3)
        :return: None
        """
        row_pos = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_pos)

        for index, info in enumerate(data):
            self.tableWidget.setItem(row_pos, index, QTableWidgetItem(info))
            self.tableWidget.scrollToBottom()

    def addToRecentTableWidget(self, data):  # slot >> trigger singal
        """
        Use this method if you have TableWidget to add items in rows
        :param data: tuple of values (1, 2, 3)
        :return: None
        """
        row_pos = self.recent_tablewidgeet.rowCount()
        self.recent_tablewidgeet.insertRow(row_pos)

        for index, info in enumerate(data):
            self.recent_tablewidgeet.setItem(row_pos, index, QTableWidgetItem(info))
            self.recent_tablewidgeet.scrollToBottom()

    def confirmMessage(self, title, text, mode="question"):
        """
        use this method to show a confirm dialog
        :param title: message title
        :param text: message content
        :param mode: question or warning type - default is question
        :return: True if yes clicked - False if No clicked
        """
        if mode == "warning":
            re = QMessageBox.warning(self, title, text, QMessageBox.Yes | QMessageBox.No)
        else:
            re = QMessageBox.question(self, title, text, QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:
            return True
        else:
            return False

    def error_message(self, title, text):
        QMessageBox.critical(self, title, text, QMessageBox.Ok)

    def ok_message(self, title, text):
        QMessageBox.information(self, title, text, QMessageBox.Ok)


    def saveDialog(self):
        """:return saving path"""
        path = QFileDialog.getSaveFileName(self, "save data", "data", "*.csv")
        return path[0]

    def openFileDialog(self):
        """:return a tuple (path, file extension)"""
        path = QFileDialog.getOpenFileName(self, "open the excel sheet", "", "*.xlsx *.csv")
        self.sheet_le.setText(path[0])

    def openMultiFileDialog(self):
        """:return a tuple (path, file extension)"""
        path = QFileDialog.getOpenFileNames(self, "open the excel sheet", "", "*.txt")
        if len(path[0]) > 0:
            self.multi_messages_le.setText(str(path[0]))

    def getImagePath(self):
        """:return a tuple (list of paths, file extension)"""
        path = QFileDialog.getOpenFileNames(self, "choose a media file", "")
        if len(path[0]) > 0:
            self.attachments_le.setText(str(path[0]))

    def appendToPlainTextBox(self):
        self.message_text.insertPlainText("{name}")

    def appendToPlainTextBox_newmessage(self):
        self.message_text.insertPlainText("\n\n\n{new message}\n\n")
        self.message_text.moveCursor(QtGui.QTextCursor.End)

    def appendToPlainTextBox_extraVar(self):
        self.message_text.insertPlainText("{variable}")

    def changeStateToStopped(self):
        self.statusbar.showMessage(f"   >> Stopping in progress... <<")
        self.state = "stopped"

    def loadInterfaceValues(self, data):
        """
        :param data: list of tuples
        :return: None
        """
        if len(data) != 0:
            values = data[-1]
            self.sheet_le.setText(values[0])
            self.messages_sbox.setValue(int(values[1]))
            self.minutes_sbox.setValue(int(values[2]))
            if values[3] == 1:
                self.checkBox.setChecked(True)
            else:
                self.checkBox.setChecked(False)
            self.attachments_le.setText(values[4])
            self.message_text.setPlainText(values[5])
            self.contactCard_le.setText(values[6])



