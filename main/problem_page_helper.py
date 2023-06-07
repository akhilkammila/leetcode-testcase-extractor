import time
from csv import DictReader
from locators import SingleProblemPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ProblemPageHelper:
    # Count lines
    def getLineCount(driver):
        parent_div = driver.find_element(By.XPATH, SingleProblemPage.EDITOR_XPATH)
        last_child_with_text = parent_div.find_elements(By.XPATH, './/div[text()]')[-1]
        result = int(last_child_with_text.text)
        return result

    # Wait conditions
    def secondLastLineContainsDef(driver):
        def condition(driver):
            numLines = ProblemPageHelper.getLineCount(driver)
            secondLastLineText = driver.find_elements(By.CLASS_NAME, SingleProblemPage.EDITOR_LINE_CLASS)[numLines-2].text
            return 'def' in secondLastLineText
        return condition

    def linesCountEquals(driver, expected_lines):
        def condition(driver):
            return ProblemPageHelper.getLineCount(driver) == expected_lines
        return condition
    
    def onlyOneEditor(driver):
        def condition(driver):
            editors = driver.find_elements(By.CSS_SELECTOR, SingleProblemPage.EDITOR_CSS)
            return len(editors) == 1
        return condition