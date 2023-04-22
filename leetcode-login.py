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

# Setup for device
if platform.system() == "Windows":
    MOD_KEY = Keys.CONTROL
else:
    MOD_KEY = Keys.COMMAND

# get hidden auth variables
from auth import gmail
from auth import pswd

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30) #times out on 30 seconds
actions = ActionChains(driver)

leetcode_login_link = "https://leetcode.com/accounts/login/"

def sign_in():
    driver.get(leetcode_login_link)
    driver.find_element(By.NAME, "login").send_keys(gmail)
    driver.find_element(By.NAME, "password").send_keys(pswd)
    driver.find_element(By.ID, "signin_btn").click()
    wait.until_not(EC.title_contains("Login")) #fully logs in, waits until goes to next page

def load_problem(prob_link):
    driver.get(prob_link)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"view-lines monaco-mouse-cursor-text\"]")))

def switch_to_python():
    driver.find_element(By.XPATH, "//div[text()='C++']").click()
    driver.find_element(By.XPATH, "//div[text()='Python3']").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"view-lines monaco-mouse-cursor-text\"]")))

def problem_setup():
    # Setup default submission
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"view-line\"]")))
    text="if (False): return"
    code_box_divs = driver.find_elements(By.CSS_SELECTOR, "div[class=\"view-line\"]")
    actions.move_to_element(code_box_divs[-1]).click().send_keys(Keys.END + Keys.ENTER + text).perform()

    # Submit
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

# Stores some paths to elements
def get_element():
    code_box = driver.find_element(By.CSS_SELECTOR, "div[class=\"view-lines monaco-mouse-cursor-text\"]")
    code_box_divs = driver.find_elements(By.CSS_SELECTOR, "div[class=\"view-line\"]")
    code_box_divs = code_box.find_elements(By.XPATH, "./*")


def pause():
    a = input()


if __name__ == "__main__":
    sign_in()
    load_problem("https://leetcode.com/problems/two-sum/")
    switch_to_python()
    problem_setup()
    pause()
