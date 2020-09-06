import os
from time import sleep
import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class WhatsApp:
    def __init__(self):
        self.main_path = os.path.abspath(os.path.dirname(__file__))
        self.data_path = os.path.join(self.main_path, "Data")
        self.chromdriver_path = os.path.join(self.data_path, "chromedriver")
        self._msg_input = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'



    def open(self, contact_name):
        """
        :param contact_name: string
        :return: the window object
        """
        chrome_options = Options()
        chrome_options.add_argument(r'--user-data-dir=' + os.path.join(self.data_path, contact_name))

        window = webdriver.Chrome(self.chromdriver_path, options=chrome_options)
        window.get("https://web.whatsapp.com/")
        # waiting for the whatsapp to login
        WebDriverWait(window, 1000).until(ec.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div[4]/div/div/div[2]/h1')))
        return window
