import os
from selenium import webdriver
from selenium.webdriver import ActionChains, FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, InvalidArgumentException, StaleElementReferenceException, \
    NoSuchElementException
import random
import shutil
import platform
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from multiprocessing import Queue


if platform.system() == "Darwin":
    browserData = f"{os.path.expanduser('~')}/Library/WhatsappSenderData/Data/WhatsappLogin"
    browserData_firefox = f"{os.path.expanduser('~')}/Library/WhatsappSenderData/Data/WhatsappLoginFirefox"
    data_folder = f"{os.path.expanduser('~')}/Library/WhatsappSenderData/Data"
else:
    data_folder = os.path.join("C:\\ProgramData", "Data")
    browserData_firefox = os.path.join(data_folder, "WhatsappLoginFirefox")
    browserData = os.path.join(data_folder, "WhatsappLogin")

os.system(f'mkdir "{browserData_firefox}"')


class WhatsApp:
    browserAuthDirectory = browserData  # browser data location
    firefoxProfilePath = browserData_firefox  # browser data location
    # _chromedriverPath = chromedriver  # chromedriver.exe location
    _dataFolder = data_folder
    # delaying in seconds
    # this is the range of seconds that will be delayed between messages
    _minSeconds = 5
    _maxSeconds = 30
    _handle = None
    window = None
    recent_contacts = []
    _search_bar = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    _sbar_arrow = '//*[@id="side"]/div[1]/div/button'
    _profile_header = '//*[@id="main"]/header/div[2]/div/div/span'
    _group_pos = '//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]' \
                 '/div[2]/div/div/div/div/div[2]/div[1]/div/span'
    _msg_input = '//*[@id="main"]/footer//div[contains(@class, "copyable-text") and contains(@class, "selectable-text") and @spellcheck]'
    _cancel_x = '//*[@id="side"]/div[1]/div/span/button'
    _attachment = '//span[@data-icon="clip"]/parent::div'
    # self._attachment called first then wait for self._imageinput to appear
    _imageinput = 'ul > li:first-child input'  # CSS Selector
    # this button appears when the photo is loaded
    _sendimagebtn = '//span[@data-icon="send-light"]'
    _sendimagebtn2 = '//span[@data-icon="send"]'
    # Contact Card sending
    _attachContactBtn = 'ul > li:nth-child(4) button'  # CSS Selector
    _contactSearchBar = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/label/div/div[2]'
    _sendBtn = '//span[@data-icon="send"]/parent::div'
    _xBtn = '//span[@data-icon="x"]/ancestor::header/descendant::button'
    # phone not connected
    phone_alert = '//span[@data-icon="alert-phone"]'
    computer_alert = '//span[@data-icon="alert-computer"]'
    backArrow_button = '//*[@id="side"]/div[1]/div/button'
    caption_input = '//span//div[contains(@class, "selectable-text")and contains(@class, "copyable-text")]'

    def __init__(self, signals_obj):
        self.sig = signals_obj

    def logout_btn(self):
        shutil.rmtree(self.browserAuthDirectory)

    def open(self, browser):
        """
        :return: the window object
        """
        if self._handle is None:
            if browser == "chrome":
                chrome_options = Options()
                chrome_options.add_argument(r'--user-data-dir=' + self.browserAuthDirectory)
                args = ["hide_console", ]
                self.window = webdriver.Chrome(ChromeDriverManager().install(),
                                               options=chrome_options, service_args=args)
            else:
                # self._window = webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=FirefoxProfile(self.firefoxProfilePath))
                self.window = webdriver.Firefox(executable_path=GeckoDriverManager().install())

            self.window.get("https://web.whatsapp.com/")
            self._handle = self.window.current_window_handle
            # waiting for the whatsapp to login
            WebDriverWait(self.window, 1000).until(ec.presence_of_element_located((
                By.XPATH, '//*[@id="app"]/div/div/div[4]/div/div/div[2]/h1')))
            sleep(1)

            return self.window
        else:
            # if browser was opened before >> switch focus to it
            self.window.switch_to.window(self._handle)
            return self.window

    def close(self):
        self.window.quit()

    def number_search(self, number):
        """
        opens the selected number chat if found
        :param number: phone number to search in whatsapp
        :return: False - if number not found on phone book
        """
        number = number.replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
        search_bar = self.window.find_element_by_xpath(self._search_bar)
        if search_bar.text != "":
            self.window.find_element_by_xpath(self.backArrow_button).click()
        sleep(1)
        search_bar.send_keys(number)
        # checking if results appear
        try:
            WebDriverWait(self.window, 10).until(ec.visibility_of_element_located((
                By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]')))
        except TimeoutException:
            return False
        sleep(random.randint(3, 5))

        search_bar.send_keys(Keys.ENTER)
        # check if number was found or not
        if search_bar.text != "":
            return False


    def sending(self, message):
        """
        when the chat is opened with number_search method, this method is called to send the message
        :param message: text message to be sent
        :return: None
        """
        message_input = self.window.find_element_by_xpath(self._msg_input)
        message_input.send_keys(message)
        message_input.send_keys(Keys.ENTER)

    def sending_sameFormat(self, message):
        message_lines = message.split("\n")
        try:
            message_input = self.window.find_element_by_xpath(self._msg_input)
        except NoSuchElementException:
            # SHOWING THE WHATSAPP WINDOW TO AVOID ELEMENT NOT FOUND BUG
            self.window.switch_to.window(self.window.window_handles[0])
            sleep(1)
            message_input = self.window.find_element_by_xpath(self._msg_input)
        actions = ActionChains(self.window)
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

    def _sending_sameFormat_captionInput(self, message):
        message_lines = message.split("\n")
        message_input = self.window.find_element_by_xpath(self.caption_input)
        actions = ActionChains(self.window)
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

    def sending_image(self, paths):
        multiple_paths = paths[0]
        if len(paths) > 1:
            for path in paths[1:]:
                multiple_paths += "\n" + path
        try:
            sleep(random.randint(1, 3))
            self.window.find_element_by_xpath(self._attachment).click()
            sleep(random.randint(1, 2))
        except Exception as e:
            print(e)
            print("clicking attachment button error")
            return False
        # waits for the image button to appear then send the path
        try:
            WebDriverWait(self.window, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, self._imageinput))).send_keys(multiple_paths)
        except TimeoutException:
            print("image input button didn't appear")
            return False
        except InvalidArgumentException:
            print("image path is not correct")
            return False

        sleep(random.randint(2, 3))
        try:
            try:  # fixing a bug - xpath changed
                WebDriverWait(self.window, 10).until(
                    ec.presence_of_element_located((By.XPATH, self._sendimagebtn2))).click()
            except TimeoutException:
                WebDriverWait(self.window, 10).until(
                    ec.presence_of_element_located((By.XPATH, self._sendimagebtn))).click()
        except TimeoutException:
            print("send btn didn't appear")
            print("choosed image maybe not supported")
            return False
        sleep(random.randint(3, 6))

    def sending_image_with_caption(self, paths, message):
        multiple_paths = paths[0]
        if len(paths) > 1:
            for path in paths[1:]:
                multiple_paths += "\n" + path
        try:
            sleep(random.randint(1, 3))
            self.window.find_element_by_xpath(self._attachment).click()
            sleep(random.randint(1, 3))
        except Exception as e:
            print(e)
            print("clicking attachment button error")
            return False
        # waits for the image button to appear then send the path
        try:
            WebDriverWait(self.window, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, self._imageinput))).send_keys(multiple_paths)
        except TimeoutException:
            print("image input button didn't appear")
            return False
        except InvalidArgumentException:
            print("image path is not correct")
            return False

        sleep(random.randint(2, 3))
        try:
            try:  # fixing a bug - xpath changed
                sendBtn = WebDriverWait(self.window, 10).until(
                    ec.presence_of_element_located((By.XPATH, self._sendimagebtn2)))
                self._sending_sameFormat_captionInput(message)
                sendBtn.click()
            except TimeoutException:
                sendBtn = WebDriverWait(self.window, 10).until(
                    ec.presence_of_element_located((By.XPATH, self._sendimagebtn)))
                self._sending_sameFormat_captionInput(message)
                sendBtn.click()
        except TimeoutException:
            print("send btn didn't appear")
            print("choosed image maybe not supported")
            return False
        sleep(random.randint(3, 6))

    def sending_contact(self, contact_number):
        try:
            sleep(random.randint(1, 3))
            self.window.find_element_by_xpath(self._attachment).click()
            sleep(random.randint(1, 3))
        except Exception as e:
            print(e)
            print("clicking attachment button error")
            return False
        # waits for the contact button to appear then click it
        try:
            WebDriverWait(self.window, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, self._attachContactBtn))).click()
        except TimeoutException:
            print("contact button didn't appear")
            return False
        sleep(random.randint(1, 2))
        # waiting for the search bar to appear then typing the number and hitting Enter to choose it
        try:
            searchBar_elem = WebDriverWait(self.window, 10).until(
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
            WebDriverWait(self.window, 10).until(
                ec.presence_of_element_located((By.XPATH, self._sendBtn))).click()
            sleep(2)
            # clicking the send again for the confirmation
            WebDriverWait(self.window, 10).until(
                ec.presence_of_element_located((By.XPATH, self._sendBtn))).click()
        except TimeoutException:
            print("sending btn didn't appear in sending contact card")
            self.window.find_element_by_xpath(self._xBtn).click()
            return False

    def unsaved_number_search(self, number):
        """
        this will open the selected number chat via whatsapp shared api
        *note : this is called when the number is not found in phone book
        :param number: whatsapp phone number
        :return: False - if number has no whatsapp
        """

        # added sleeps to fix a bug with get()
        number = number.replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
        url = f"https://web.whatsapp.com/send?phone={number}"
        sleep(2)
        self.window.get(url)
        sleep(2)
        # sometimes an alert pops up!
        try:
            self.window.switch_to.alert.accept()
        except Exception:
            pass

        profile_side_div = '//div[@id="side"]/header'   # TO CHECK IF LOADING IS DONE OR NOT
        starting_chat_loading_div = '//*[@role="status" and @viewBox and @height and @width and @class]'
        ok_btn = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div'
        # WAITING FOR LOADING TO FINISH
        # (FUTURE FIX) - this loading may stay forever... I need to take care of this
        WebDriverWait(self.window, 1000).until(ec.visibility_of_element_located(
            (By.XPATH, profile_side_div)))
        sleep(2)
        # WAIT FOR "starting chat" TO DISAPPEAR
        WebDriverWait(self.window, 3600).until(ec.invisibility_of_element_located((By.XPATH, starting_chat_loading_div)))
        # CHECK IF NOT FOUND OK BUTTON APPEARED
        try:
            WebDriverWait(self.window, random.randint(2, 3)).until(
                ec.visibility_of_element_located((
                    By.XPATH, ok_btn))).click()
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
            self.window.find_element_by_xpath(self.phone_alert)
            print("PHONE IS NOT CONNECTED!!")
            return False
        except Exception:
            pass

        try:
            print("checking on computer connection..")
            self.window.find_element_by_xpath(self.computer_alert)
            print("Computer IS NOT CONNECTED!!")
            return False
        except Exception:
            pass

    @staticmethod
    def is_it_today(date):
        """
        :param date: datetime object
        :return: True if today - None if not today or empty cell
        """
        if date is not None:
            today = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
            if date == today:
                return True

    @staticmethod
    def startTime_check(time):
        """
        :param time: datetime.time object
        :return: True if it's now or past time & returns total seconds if it's future time (to use in sleep method)
        """
        if time is None:
            return None
        now = datetime.now()
        time = datetime(year=now.year, month=now.month, day=now.day, hour=time.hour, minute=time.minute)
        if now >= time:
            return True
        else:
            sleep_duration = time - now
            if sleep_duration.days < 0:
                sleep_duration = time - now
            return sleep_duration.total_seconds()

    @staticmethod
    def endTime_check(time, start_time):
        """
        :param start_time: datetime.time object
        :param time: datetime.time object
        :return: True if current hour is less than end time & returns total seconds till start time on next day (to use in sleep method)
        """
        if time is None:
            return None
        now = datetime.now()
        time = datetime(year=now.year, month=now.month, day=now.day, hour=time.hour, minute=time.minute)
        start_time = datetime(year=now.year, month=now.month, day=now.day, hour=start_time.hour,
                              minute=start_time.minute)
        if now < time:
            return True
        else:
            day_seconds = 86400
            sleep_duration = now - start_time
            sleep_duration = day_seconds - sleep_duration.total_seconds()
            return sleep_duration

    def get_window_object(self):
        return self.window

    def extract_recent(self) -> list:
        """
        this method extracts the unsaved numbers in recent chats
        :return: list or strings
        """
        # SCROLLING TO TOP FIRST
        self.window.execute_script('document.getElementById("pane-side").scrollTop = 0;')
        # CLEARING SEARCHBAR
        search_bar = self.window.find_element_by_xpath(self._search_bar)
        if search_bar.text != "":
            self.window.find_element_by_xpath(self.backArrow_button).click()
        sleep(1)
        number_xpath = '//div[2]/div[@role="gridcell"]//span[@class and @dir="auto" and starts-with(@title, "+")]'
        contacts = []
        stop_counter = 0
        while True:
            if stop_counter >= 3:
                return contacts
            elements = self.window.find_elements_by_xpath(number_xpath)
            added_new_phone = False
            # SCRAPING NUMBERS
            for elem in elements:
                try:
                    phone = elem.get_attribute("title")
                    if phone not in contacts:
                        added_new_phone = True
                        contacts.append(phone)
                        self.sig.recent_extracted.emit(phone)
                        self.recent_contacts.append(["Recent Contact", self.clean_number(phone)])
                except StaleElementReferenceException:
                    print("stale occured!!!!")
                    self.extract_recent()

            # SCROLLING
            self.window.execute_script('document.getElementById("pane-side").scrollBy(0 , 1000);')
            sleep(2)
            # INCREASE COUNTER IF NO MORE NEW RESULTS SHOWN - THAT MEANS WE REACHED THE END AND NO MORE TO SCROLL
            if added_new_phone is False:
                stop_counter += 1

    @staticmethod
    def clean_number(phone:str) -> str:
        return phone.replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "").replace("/","").replace("\\", "")
