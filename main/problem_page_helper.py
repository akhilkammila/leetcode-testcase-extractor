import time
from csv import DictReader
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ProblemPageHelper:
    def linesCountEquals(driver, expected_lines):
        def condition(driver):
            parent_div = driver.find_element(By.XPATH, '//*[@id="editor"]/div[4]/div[1]/div/div/div[1]/div[1]/div[3]')
            last_child_with_text = parent_div.find_elements(By.XPATH, './/div[text()]')[-1]
            print(last_child_with_text.text, flush=True)
            return int(last_child_with_text.text) == expected_lines
        return condition