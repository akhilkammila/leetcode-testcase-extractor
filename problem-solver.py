import time
import random
import platform
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

from auth import AuthInfo
from locators import LoginPage
from locators import ProblemPage

# class ProblemSolver:
#     def __init__(self, prob_link, waitTime=30):
#         self.driver = webdriver.Chrome()
#         self.wait = WebDriverWait(self.driver, waitTime) #times out on 30 seconds
#         self.prob_link = prob_link

#     def load_problem(self):
#         self.driver.get(self.prob_link)
#         self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"view-lines monaco-mouse-cursor-text\"]")))