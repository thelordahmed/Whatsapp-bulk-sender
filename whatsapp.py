import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException, WebDriverException, \
    InvalidArgumentException, NoSuchElementException
import random
import requests, zipfile, io
from features_controller import system
import shutil


class WhatsApp:
    browserAuthDirectory = "Data/WhatsappLogin"  # browser data location
    _chromedriverPath = "Data/chromedriver" # chromedriver.exe location
    _dataFolder = "Data"
    # delaying in seconds
    # this is the range of seconds that will be delayed between messages
    _minSeconds = 5
    _maxSeconds = 30
    _chrome_options = Options()
    _chrome_options.add_argument(r'--user-data-dir=' + browserAuthDirectory)

    def __init__(self):
        self._handle = None
        self._window = None
        self._search_bar = '//*[@id="side"]/div[1]/div/label/div/div[2]'
        self._sbar_arrow = '//*[@id="side"]/div[1]/div/button'
        self._profile_header = '//*[@id="main"]/header/div[2]/div/div/span'
        self._group_pos = '//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]' \
                          '/div[2]/div/div/div/div/div[2]/div[1]/div/span'
        self._msg_input = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        self._cancel_x = '//*[@id="side"]/div[1]/div/span/button'
        self._attachment = '//span[@data-icon="clip"]/parent::div'
        # self._attachment called first then wait for self._imageinput to appear
        self._imageinput = 'ul > li:first-child input'  # CSS Selector
        # this button appears when the photo is loaded
        self._sendimagebtn = '//span[@data-icon="send-light"]'
        self._sendimagebtn2 = '//span[@data-icon="send"]'
        # Contact Card sending
        self._attachContactBtn = 'ul > li:last-child button'  # CSS Selector
        self._contactSearchBar = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/label/div/div[2]'
        self._sendBtn = '//span[@data-icon="send"]/parent::div'
        self._xBtn = '//span[@data-icon="x"]/ancestor::header/descendant::button'

        # phone not connected
        self.phone_alert = '//span[@data-icon="alert-phone"]'
        self.computer_alert = '//span[@data-icon="alert-computer"]'
        self.backBlue_btn = '//span[@data-icon="back-blue"]/ancestor::button'
        self.backBlue_btn2 = '//span[@data-icon="search"]/ancestor::button'

    # updating chromedriver automatically
    @staticmethod
    def _chromedriver_update(zip_extract_path):
        print("chromedriver is outdated! .. updating...")
        stable_ver = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE").text
        file = requests.get(f"https://chromedriver.storage.googleapis.com/{stable_ver}/chromedriver_win32.zip")
        z = zipfile.ZipFile(io.BytesIO(file.content))
        z.extractall(zip_extract_path)

    def _chromedriver_update_mac(self):
        file_name = "chromedriver_macos.zip"
        file_path = os.path.join(self._dataFolder, file_name)
        print("chromedriver is outdated! .. updating...")
        stable_ver = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE").text
        file = requests.get(f"https://chromedriver.storage.googleapis.com/{stable_ver}/chromedriver_mac64.zip")
        with open(file_path, "wb") as f:
            f.write(file.content)
        os.system(f"unzip {file_path} -d {self._dataFolder}")
        sleep(2)
        os.system(f"rm {file_path}")

    def logout_btn(self):
        shutil.rmtree(self.browserAuthDirectory)

    def open(self):
        """
        :return: the window object
        """
        args = ["hide_console", ]
        if self._handle is None:
            try:
                self._window = webdriver.Chrome(self._chromedriverPath,
                                                options=self._chrome_options, service_args=args)
            except SessionNotCreatedException and WebDriverException:
                if system == "mac":
                    self._chromedriver_update_mac()
                    self._window = webdriver.Chrome(self._chromedriverPath,
                                                    options=self._chrome_options, service_args=args)
                else:
                    self._chromedriver_update(self._dataFolder)
                    self._window = webdriver.Chrome(self._chromedriverPath,
                                                    options=self._chrome_options, service_args=args)

            self._window.get("https://web.whatsapp.com/")
            self._handle = self._window.current_window_handle
            # waiting for the whatsapp to login
            WebDriverWait(self._window, 1000).until(ec.presence_of_element_located((
                By.XPATH, '//*[@id="app"]/div/div/div[4]/div/div/div[2]/h1')))
            return self._window
        else:
            # if browser was opened before >> switch focus to it
            self._window.switch_to.window(self._handle)
            return self._window

    def close(self):
        self._window.quit()

    def number_search(self, number):
        """
        opens the selected number chat if found
        :param number: phone number to search in whatsapp
        :return: False - if number not found on phone book
        """
        search_bar = self._window.find_element_by_xpath(self._search_bar)
        try:    # fixing a bug -- back button xpath changed
            self._window.find_element_by_xpath(self.backBlue_btn).click()
        except NoSuchElementException:
            self._window.find_element_by_xpath(self.backBlue_btn2).click()

        sleep(1)
        search_bar.send_keys(number)
        # checking if results appear
        try:
            WebDriverWait(self._window, 10).until(ec.visibility_of_element_located((
                By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]')))
        except TimeoutException:
            return False
        sleep(random.randint(3, 5))

        contact_xpath = '//*[@id="pane-side"]//div[2]/div[1]/div[1]/span'  # this xpath chooses only the contact chat; not groups or messages
        try:
            self._window.find_element_by_xpath(contact_xpath).click()
        except Exception:
            return False

    def sending(self, message):
        """
        when the chat is opened with number_search method, this method is called to send the message
        :param message: text message to be sent
        :return: None
        """
        message_input = self._window.find_element_by_xpath(self._msg_input)
        message_input.send_keys(message)
        message_input.send_keys(Keys.ENTER)


    def sending_sameFormat(self, message):
        message_lines = message.split("\n")
        message_input = self._window.find_element_by_xpath(self._msg_input)
        actions = ActionChains(self._window)
        actions.move_to_element(message_input)
        actions.click()
        for line in message_lines:
            actions.send_keys(line)
            actions.key_down(Keys.SHIFT)
            actions.key_down(Keys.ENTER)
            actions.key_up(Keys.SHIFT)
            actions.key_up(Keys.ENTER)
        actions.perform()
        sleep(1)
        message_input.send_keys(Keys.ENTER)


    def sending_image(self, paths):
        for path in paths:
            try:
                sleep(random.randint(1,3))
                self._window.find_element_by_xpath(self._attachment).click()
                sleep(random.randint(1,3))
            except Exception as e:
                print(e)
                print("clicking attachment button error")
                return False
            # waits for the image button to appear then send the path
            try:
                WebDriverWait(self._window, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, self._imageinput))).send_keys(path)
            except TimeoutException:
                print("image input button didn't appear")
                return False
            except InvalidArgumentException:
                print("image path is not correct")
                return False

            sleep(random.randint(2,3))
            try:
                try:    # fixing a bug - xpath changed
                    WebDriverWait(self._window, 10).until(ec.presence_of_element_located((By.XPATH, self._sendimagebtn2))).click()
                except TimeoutException:
                    WebDriverWait(self._window, 10).until(ec.presence_of_element_located((By.XPATH, self._sendimagebtn))).click()
            except TimeoutException:
                print("send btn didn't appear")
                print("choosed image maybe not supported")
                return False
            sleep(random.randint(3,6))

    def sending_contact(self, contact_number):
        try:
            sleep(random.randint(1,3))
            self._window.find_element_by_xpath(self._attachment).click()
            sleep(random.randint(1,3))
        except Exception as e:
            print(e)
            print("clicking attachment button error")
            return False
        # waits for the contact button to appear then click it
        try:
            WebDriverWait(self._window, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, self._attachContactBtn))).click()
        except TimeoutException:
            print("contact button didn't appear")
            return False
        sleep(random.randint(1, 2))
        # waiting for the search bar to appear then typing the number and hitting Enter to choose it
        try:
            searchBar_elem = WebDriverWait(self._window, 10).until(
                ec.presence_of_element_located((By.XPATH, self._contactSearchBar)))
            searchBar_elem.send_keys(contact_number)
            sleep(5)
            searchBar_elem.send_keys(Keys.ENTER)
        except TimeoutException:
            print("can't find contact search bar when sending a contact card")
            return False
        sleep(1)
        # waiting for the send btn to appear then clicking it
        try:
            WebDriverWait(self._window, 10).until(
                ec.presence_of_element_located((By.XPATH, self._sendBtn))).click()
            sleep(2)
            # clicking the send again for the confirmation
            WebDriverWait(self._window, 10).until(
                ec.presence_of_element_located((By.XPATH, self._sendBtn))).click()
        except TimeoutException:
            print("sending btn didn't appear in sending contact card")
            self._window.find_element_by_xpath(self._xBtn).click()
            return False


    def unsaved_number_search(self, number):
        """
        this will open the selected number chat via whatsapp shared api
        *note : this is called when the number is not found in phone book
        :param number: whatsapp phone number
        :return: False - if number has no whatsapp
        """
        # added sleeps to fix a bug with get()
        url = f"https://web.whatsapp.com/send?phone={number}"
        sleep(2)
        self._window.get(url)
        sleep(2)
        # sometimes an alert pops up!
        try:
            self._window.switch_to.alert.accept()
        except Exception:
            pass

        ok_btn = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div'
        loading_div = '//*[@id="startup"]/div'
        # waiting for loading div to disappear
        WebDriverWait(self._window, 60).until(ec.invisibility_of_element_located(
            (By.XPATH, loading_div)))
        sleep(2)
        try:
            # TODO -- "trying to connect phone" may appear, I need to take care of this
            WebDriverWait(self._window, random.randint(5, 10)).until(ec.visibility_of_element_located(
                (By.XPATH, ok_btn))).click()
            return False
        except TimeoutException:
            pass

    def connectionCheck(self):
        """
        if this element was found - means there's no connection
        :return: False - if no connection
        """
        try:
            print("checking on phone connection..")
            self._window.find_element_by_xpath(self.phone_alert)
            print("PHONE IS NOT CONNECTED!!")
            return False
        except Exception:
            pass

        try:
            print("checking on computer connection..")
            self._window.find_element_by_xpath(self.computer_alert)
            print("Computer IS NOT CONNECTED!!")
            return False
        except Exception:
            pass
