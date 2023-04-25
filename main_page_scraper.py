from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from auth import AuthInfo
from locators import LoginPage
from locators import ProblemPage

class MainPageScraper:
    def __init__(self, waitTime=30):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, waitTime)

    def login(self):
        self.driver.get(LoginPage.URL)
        self.wait.until(EC.title_is(LoginPage.TITLE))
        self.driver.find_element(By.NAME, LoginPage.USERNAME_NAME).send_keys(AuthInfo.gmail)
        self.driver.find_element(By.NAME, LoginPage.PASSWORD_NAME).send_keys(AuthInfo.pswd)
        self.driver.find_element(By.ID, LoginPage.SIGN_IN_BUTTON_ID).click()
        self.wait.until_not(EC.title_is(LoginPage.TITLE))
    
    # Prints all the problems on the main problem's page
    def get_problems_on_page(self):
        self.driver.get(ProblemPage.URL)
        self.wait.until(EC.title_is(ProblemPage.TITLE))

        possible_problems = self.driver.find_elements(By.CSS_SELECTOR, ProblemPage.LINK_TO_PROBLEM_CSS)
        for problem in possible_problems:
            if problem.text.__contains__('.'):
                print(problem.text)
                print(problem.get_attribute('href'))