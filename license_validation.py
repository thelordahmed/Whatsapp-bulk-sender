import os
import platform
import requests
from requests.exceptions import ConnectionError
from getmac import get_mac_address as gma


class License:
    def __init__(self, api_url, view_object):
        self.api_url = api_url
        self.view = view_object
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
                res = requests.put(f"{self.api_url}/key/{key}/{mac}").json()
                self.license_input.setText(key)
                if res["response"] == "expired":
                    self.view.license_status_label.setText("Sorry, this license has expired. \nplease visit link below to renew your key\n\nhttps://www.fiverr.com/share/5ADL24")
                    self.view.license_btn.setEnabled(True)
                elif res["response"] == "invalid":
                    self.view.license_status_label.setText("Invalid key. \nplease visit link below to order a valid key\n\nhttps://www.fiverr.com/share/5ADL24 ")
                    self.view.license_btn.setEnabled(True)
                elif res["response"] == "different device":
                    self.view.license_status_label.setText("Sorry, this key is registed to another device. \nplease contact the seller.")
                    self.view.license_btn.setEnabled(True)
                elif res["response"] == "valid":
                    # saving the key if it's valid
                    if platform.system() == "Darwin":
                        data_folder = f"{os.path.expanduser('~')}/Library/WhatsappSenderData/Data"
                    else:
                        data_folder = "Data"
                    with open(os.path.join(data_folder, "license_key.txt"), "w") as f:
                        f.write(key)

                    # increasing online counter
                    requests.put(f"{self.api_url}/connected/increase")
                    self.show()
                    current_title = self.view.windowTitle()
                    self.view.setWindowTitle(f"{current_title} ---- Expire Date: {res['date']}")
        except ConnectionError:
            self.view.license_status_label.setText("Connection Error!")
            self.view.license_btn.setEnabled(True)





