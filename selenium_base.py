import time
import pyperclip
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from undetected_chromedriver import Chrome, ChromeOptions

from auth import GoogleLogin
from locators import Google

from pyvirtualdisplay import Display

class SeleniumBase:
    def __init__(self, waitTime):
        display = Display(visible=0, size=(800, 600))
        display.start()

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')

        self.driver = WebDriver(options=options)
        self.wait = WebDriverWait(self.driver, waitTime)
    
    def undetected_init(self, waitTime):
        display = Display(visible=0, size=(800, 600))
        display.start()

        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')

        self.driver = Chrome(options=options)
        self.wait = WebDriverWait(self.driver, waitTime)

    # Getters (with waiting)
    def get_by_text(self, element_type, text):
        xpath = "//" + element_type + "[text()= '" + text + "']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return self.driver.find_element(By.XPATH, xpath)
    
    def get_by_id(self, element_type, id):
        self.wait.until(EC.element_to_be_clickable((By.ID, id)))
        return self.driver.find_element(By.ID, id)
    
    def get_by_href(self, href):
        xpath = "//a[@href='" + href + "']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return self.driver.find_element(By.XPATH, xpath)
    
    def get_by_link_text(self, text):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, text)))
        return self.driver.find_element(By.LINK_TEXT, text)
    
    # Operators
    def click(self, element):
        self.driver.execute_script("arguments[0].click();", element)
    
    def send_keys(self, element, keys):
        self.click(element)
        self.driver.switch_to.active_element.send_keys(keys)