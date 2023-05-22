import time
import pyperclip
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from auth import GoogleLogin
from locators import LeetcodeLogin
from locators import Google
from selenium_base import SeleniumBase

class LoginBot(SeleniumBase):
    def google_login(self):
        self.driver.get(Google.URL)
        self.send_keys(self.get_by_text("div", "Email or phone"), GoogleLogin.gmail + "\n")
        self.send_keys(self.get_by_text("div", "Enter your password"), GoogleLogin.pswd + "\n")
        time.sleep(1) #ensure that fully logged into google before continuing
    
    def leetcode_login(self):
        self.driver.get(LeetcodeLogin.URL)