import os
import platform
import webbrowser
from json.decoder import JSONDecodeError
from features_controller import version
import requests
from requests.exceptions import ConnectionError
from getmac import get_mac_address as gma


invalid_key_msg = "Invalid Key!"
expired_key_msg = "Sorry, this license has expired."
registered_key_msg = "Sorry, this key is registed to another device. \nplease contact the seller."


class License:
    def __init__(self, api_url, view_object):
        self.api_url = api_url
        self.view = view_object
        self.download_page = "https://softwarekeys.herokuapp.com/download"
        self.license_frame = self.view.license_frame
        self.license_input = self.view.license_le
        self.license_button = self.view.license_btn
        self.status_label = self.view.license_status_label

        self.license_button.clicked.connect(lambda: self.validate(None))

    def show(self):
        # hide license frame
        self.view.license_frame.hide()
        # show hidden interface
        self.view.main_frame.show()
        self.view.buttons_frame.show()
        self.view.logout_btn.show()

    def validate(self, key=None):
        # if key is None, that means this method was called on app start with pre-saved key
        if key is None:
            key = self.license_input.text().strip()
        try:
            if key != "":
                self.view.license_btn.setDisabled(True)
                mac = gma()
                try:
                    res = requests.put(f"{self.api_url}/key/{key}/{mac}").json()
                except JSONDecodeError:
                    self.view.license_status_label.setText(invalid_key_msg)
                    self.view.license_btn.setEnabled(True)
                    return False
                self.license_input.setText(key)
                if res["response"] == "expired":
                    self.view.license_status_label.setText(expired_key_msg)
                    self.view.license_btn.setEnabled(True)
                elif res["response"] == "invalid":
                    self.view.license_status_label.setText(invalid_key_msg)
                    self.view.license_btn.setEnabled(True)
                elif res["response"] == "different device":
                    self.view.license_status_label.setText(registered_key_msg)
                    self.view.license_btn.setEnabled(True)
                elif res["response"] == "valid":
                    # saving the key if it's valid
                    if platform.system() == "Darwin":
                        data_folder = f"{os.path.expanduser('~')}/Library/WhatsappSenderData/Data"
                    else:
                        data_folder = r"C:\ProgramData"
                    with open(os.path.join(data_folder, "license_key.txt"), "w") as f:
                        f.write(key)
                    # # increasing online counter
                    # if res["user"] != "admin" and res["user"] != "admin_PC":
                    #     requests.put(f"{self.api_url}/connected/increase")
                    self.view.setWindowTitle(f"WhatsApp Bulk Sender {version} ---- Expire Date: {res['date']}")
                    self.show()
                    self.view.adjustSize()
                    if version != res["version"]:
                        confim = self.view.confirmMessage("New Update Available!", "New Update is availabe for the software!\nDo you want to download it?")
                        if confim is True:
                            webbrowser.open(self.download_page)
        except ConnectionError:
            self.view.license_status_label.setText("Connection Error!")
            self.view.license_btn.setEnabled(True)





