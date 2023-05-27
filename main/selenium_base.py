import os
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SeleniumBase:
    # Initialize
    def __init__(self, waitTime):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
    
        options.add_argument("--window-size=1920,1080")
        options.add_argument('start-maximized')

        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')

        self.driver = WebDriver(options=options)
        self.wait = WebDriverWait(self.driver, waitTime)
        self.screenshotFile = "screenshots/" + time.strftime("%Y%m%d-%H%M%S") + "/"
        os.makedirs(self.screenshotFile)
    
    # Debug functions
    def screenshot(self, filename):
        self.driver.save_screenshot(self.screenshotFile + filename)

    # Getters (with waiting)
    def get_by_text(self, element_type, text):
        xpath = "//" + element_type + "[text()= '" + text + "']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return self.driver.find_element(By.XPATH, xpath)
    
    def get_by_id(self, id):
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
        element.click()
        # self.driver.execute_script("arguments[0].click();", element)
    
    def send_keys(self, element, keys):
        self.click(element)
        self.driver.switch_to.active_element.send_keys(keys)
    
    # Copy paste operators
    def get_clipboard(self):
        trigger_script = """
        var element = document.body;
        var event = new MouseEvent('click', {
            'view': window,
            'bubbles': true,
            'cancelable': true
        });
        element.dispatchEvent(event);
        """
        self.driver.execute_script(trigger_script)

        # Read the text from the clipboard using the Clipboard API
        read_script = "return navigator.clipboard.readText();"
        clipboard_text = self.driver.execute_script(read_script)
    
        return clipboard_text
    
    def set_clipboard(self, text):
        self.driver.execute_script("navigator.clipboard.writeText(arguments[0])", text)
    
    def pause(self, seconds):
        print("pausing for " + str(seconds) + " seconds", flush=True)
        time.sleep(seconds)