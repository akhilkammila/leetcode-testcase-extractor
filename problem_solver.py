import time
import pyperclip
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from auth import LeetcodeLogin
from locators import SingleProblemPage
from locators import ResultConsole

from selenium_base import SeleniumBase

class ProblemSolver(SeleniumBase):
    def __init__(self, prob_link, filePath, waitTime=10):
        super().undetected_init(waitTime)
        self.filePath = filePath
        self.prob_link = prob_link

        self.variables = []
        self.var_types = []
        self.testcases = []
        self.testcase_strings = []
        print("__init__ complete")
    
    def login(self):
        self.driver.get("https://leetcode.com/accounts/login/")
        self.wait.until_not(EC.presence_of_element_located((By.ID, "loading-screen")))
        time.sleep(5)
        self.screenshot("loginScreen.png")
        element = self.get_by_id("input", "id_login")
        self.screenshot("loginScreen2.png")
        element.send_keys(LeetcodeLogin.gmail + Keys.TAB + LeetcodeLogin.pswd + Keys.ENTER)
        self.screenshot("loginScreen3.png")
        time.sleep(5)
        self.screenshot("loginScreen4.png")


    def load_problem(self, firstTime = True):
        self.driver.get(self.prob_link)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, SingleProblemPage.EDITOR_CSS)))
        self.wait.until(lambda driver : len(driver.find_elements(By.CSS_SELECTOR, SingleProblemPage.EDITOR_LINE_CSS)) >= 2)
        if firstTime:
            self.wait.until(EC.presence_of_element_located((By.XPATH, SingleProblemPage.CPP_BUTTON_XPATH)))
    
    def switch_to_python(self):
        num_lines = len(self.driver.find_elements(By.CSS_SELECTOR, SingleProblemPage.EDITOR_LINE_CSS))
        self.driver.find_element(By.XPATH, SingleProblemPage.CPP_BUTTON_XPATH).click()
        self.driver.find_element(By.XPATH, SingleProblemPage.PYTHON_BUTTON_XPATH).click()

        self.wait.until(lambda driver : len(driver.find_elements(By.CSS_SELECTOR, SingleProblemPage.EDITOR_LINE_CSS)) != num_lines)
    
    def parse_inputs(self):
        # parse variables
        second_line = self.driver.find_elements(By.CSS_SELECTOR, SingleProblemPage.EDITOR_LINE_CSS)[1].text
        vars = [var.split(':')[0].strip() for var in second_line.split(',')[1:]]
        var_types = [var.split(':')[1].strip() for var in second_line.split(',')[1:]]

        self.variables = vars
        self.var_types = var_types
    
    def setup_file(self):
        second_line = self.driver.find_elements(By.CSS_SELECTOR, SingleProblemPage.EDITOR_LINE_CSS)[1]
        second_line.click()
        self.driver.switch_to.active_element.send_keys(Keys.COMMAND, 'a', 'c')
        
        f = open(self.filePath, "w")
        f.write(pyperclip.paste())
        f.write("\n" + " "*8 + SingleProblemPage.DEFAULT_SUBMISSION)
        f.close()
        self.testcase_strings.append(SingleProblemPage.DEFAULT_SUBMISSION)
    
    def submit(self, pauseTime=3):
        time.sleep(pauseTime)
        self.driver.find_element(By.XPATH, SingleProblemPage.SUBMIT_BUTTON_XPATH).click()
        self.wait.until_not(EC.presence_of_element_located((By.XPATH, ResultConsole.WRONG_ANSWER_XPATH)))
 
        wrong_answer_found = EC.presence_of_element_located((By.XPATH, ResultConsole.WRONG_ANSWER_XPATH))
        code_submitted_too_soon = EC.presence_of_element_located((By.XPATH, ResultConsole.CODE_SUBMITTED_TOO_SOON_XPATH))
        network_error = EC.presence_of_element_located((By.XPATH, ResultConsole.NETWORK_ERROR_XPATH))
        self.wait.until(EC.any_of(wrong_answer_found, code_submitted_too_soon, network_error))

        # If there is a wrong answer(normal), we do nothing
        try:
            self.driver.find_element(By.XPATH, ResultConsole.WRONG_ANSWER_XPATH)
        except:
            # If there is not a wrong answer, there are two cases
            # 1. we find code submitted too soon, so we resubmit
            # 2. we don't find it, so probably network error. reload, then resubmit
            try:
                self.driver.find_element(By.XPATH, ResultConsole.CODE_SUBMITTED_TOO_SOON_XPATH)
            except:
                self.load_problem(False)
            self.submit(pauseTime*1.5)
    
    def parse_testcase(self):
        def copy_following_div(div):
            div.find_elements(By.XPATH, ResultConsole.FOLLOWING_COPY_BUTTON_XPATH)[1].click()
            time.sleep(0.25)
            return pyperclip.paste()
        
        testcase_inputs = []
        for var in self.variables:
            var_div = self.driver.find_elements(By.XPATH, ResultConsole.VARIABLE_DIV_XPATH.format(var))[-1]
            var_input = var_div.find_element(By.XPATH, ResultConsole.FOLLOWING_DIV_TEXT_XPATH).text
            if 'View all' in var_input:
                var_input = copy_following_div(var_div)
            testcase_inputs.append(var_input)
        
        expected_div = self.driver.find_element(By.XPATH, ResultConsole.EXPECTED_XPATH)
        output = expected_div.find_element(By.XPATH, ResultConsole.FOLLOWING_DIV_TEXT_XPATH).text
        if 'View all' in output:
            output = copy_following_div(expected_div)
        
        conditionals = [a + " == " + b for a, b in zip(self.variables, testcase_inputs)]
        testcase_string = "if {}: return {}".format(" and ".join(conditionals), output)
        self.testcase_strings.append(testcase_string)
    
    def add_testcase(self):
        testcase = self.testcase_strings[-1]
        f = open(self.filePath, "a")
        f.write('\n' + " "*8 + testcase)
        f.close()

        f = open(self.filePath, "r")
        pyperclip.copy(f.read())
        f.close()

        self.driver.find_elements(By.CSS_SELECTOR, SingleProblemPage.EDITOR_LINE_CSS)[1].click()
        self.driver.switch_to.active_element.send_keys(Keys.COMMAND, 'a', Keys.DELETE)
        self.driver.switch_to.active_element.send_keys(Keys.COMMAND, 'v')
    
    def isSolved(self):
        return self.driver.current_url != self.prob_link
    
    def screenshot(self, filename):
        self.driver.save_screenshot("screenshots/" + filename)