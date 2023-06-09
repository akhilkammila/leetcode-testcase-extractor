import time
import os
from csv import DictReader
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_base import SeleniumBase
from problem_page_helper import ProblemPageHelper
from locators import SingleProblemPage
from locators import ResultConsole
from locators import LoginPage
from locators import ProblemPage

class ProblemSolver(SeleniumBase):
    def __init__(self, prob_link, filePath, waitTime=20):
        super().__init__(waitTime)
        self.filePath = "data/" + filePath
        self.prob_link = prob_link

        self.variables = [] #list of all the input variable names
        self.var_types = [] #input variable types
        self.output_type = ""
        self.defaultSubmission = SingleProblemPage.DEFAULT_SUBMISSION
        self.testcases = []
        self.testcase_strings = [""]
    
    def overCharacterLimit(self):
        if not os.path.isfile(self.filePath): return False

        f = open(self.filePath, "r")
        data = f.read()
        characters = len(data)
        if characters > 95000: return True

    def login(self):
        self.driver.get(LoginPage.URL)
        self.wait.until(EC.title_is(LoginPage.TITLE))
        self.wait.until_not(EC.presence_of_element_located((By.ID, LoginPage.LOADING_SCREEN_ID)))
        
        filename = "main/leetcode_cookies.csv"
        cookies = []
        with open(filename, 'r') as file:
            csv_reader = DictReader(file)
            for row in csv_reader:
                clean_row = {key.strip(): value.strip() for key, value in row.items() if key!=""}
                cookies.append(clean_row)
        for i in cookies:
            self.driver.add_cookie(i)
        
        self.driver.refresh()
        self.wait.until_not(EC.title_is(LoginPage.TITLE))

    def load_problem(self, firstTime = True):
        self.driver.get(self.prob_link)
        self.wait.until(EC.presence_of_element_located((By.XPATH, SingleProblemPage.EDITOR_XPATH)))
        self.wait.until(lambda driver : len(driver.find_elements(By.CLASS_NAME, SingleProblemPage.EDITOR_LINE_CLASS)) >= 2)
        if firstTime:
            self.wait.until(EC.presence_of_element_located((By.XPATH, SingleProblemPage.CPP_BUTTON_XPATH)))
    
    def switch_to_python(self):
        self.driver.find_element(By.XPATH, SingleProblemPage.CPP_BUTTON_XPATH).click()
        self.driver.find_element(By.XPATH, SingleProblemPage.PYTHON_BUTTON_XPATH).click()
    
    def reset_to_default(self):
        self.click(self.get_by_xpath(SingleProblemPage.RESET_BUTTON_XPATH))
        self.click(self.get_by_text("button", "Confirm"))
        
        # wait until second to last line contains "def"
        self.wait.until(ProblemPageHelper.secondLastLineContainsDef(self.driver))

    def parse_inputs(self):
        numLines = ProblemPageHelper.getLineCount(self.driver)
        # really second to last line
        second_line = self.driver.find_elements(By.CLASS_NAME, SingleProblemPage.EDITOR_LINE_CLASS)[numLines-2].text

        # parse output
        self.outputType = second_line.split('->')[1].strip()[:-1]
        if (self.outputType == "int"):
            self.defaultSubmission += " -9000000000000000"
        elif (self.outputType == "float"):
            self.defaultSubmission += " float('inf')"

        # parse inputs
        second_line = second_line[second_line.find('(')+1:second_line.find(')')]

        vars = [var.split(':')[0].strip() for var in second_line.split(',')[1:]]
        var_types = [var.split(':')[1].strip() for var in second_line.split(',')[1:]]

        self.variables = vars
        self.var_types = var_types
    
    def setup_file(self):
        # If file is already set up, skip
        if os.path.isfile(self.filePath):
            return

        second_line = self.driver.find_element(By.CLASS_NAME, SingleProblemPage.LINE_NUMBER_CLASS)
        second_line.click()
        self.driver.switch_to.active_element.send_keys(Keys.CONTROL, 'a', 'c')

        problem = self.get_clipboard()
        f = open(self.filePath, "w")
        f.write(problem)
        f.close()
    
    def parse_testcase(self):
        def copy_following_div(div):
            div.find_elements(By.XPATH, ResultConsole.FOLLOWING_COPY_BUTTON_XPATH)[1].click()
            return self.get_clipboard()
        
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

        if testcase_string == self.testcase_strings[-1]:
            raise Exception("Same Testcase")
        self.testcase_strings.append(testcase_string)
    
    def add_testcase(self):
        editor = self.driver.find_element(By.XPATH, SingleProblemPage.EDITOR_XPATH)
        editor.click()
        self.driver.switch_to.active_element.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        self.wait.until(ProblemPageHelper.linesCountEquals(self.driver, 1))

        # Write testcase to file
        testcase = self.testcase_strings[-1]
        f = open(self.filePath, "a")
        f.write('\n' + " "*8 + testcase)
        f.close()

        # Set clipboard to testcase
        f = open(self.filePath, "r")
        self.set_clipboard(f.read())
        f.close()

        # figure out why this becomes stale if i don't sleep
        time.sleep(0.5)
        self.driver.find_element(By.CLASS_NAME, SingleProblemPage.EDITOR_LINE_CLASS).click()
        self.driver.switch_to.active_element.send_keys(Keys.CONTROL, 'v')
        self.driver.switch_to.active_element.send_keys(Keys.END, Keys.ENTER, self.defaultSubmission)
    
    def submit(self, pauseTime=3):
        if pauseTime > 8:
            raise Exception("3+ Failed Submits, Likely Network Error")
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
                print("Network Error, reloading page", flush=True)
                self.load_problem(False)
            print("Code Submitted Too Soon, resubmitting", flush=True)
            self.submit(pauseTime + 2)
    
    def isSolved(self):
        return self.driver.current_url != self.prob_link