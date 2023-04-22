import time
import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# get hidden auth variables
from auth import gmail
from auth import pswd

options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

leetcode_login_link = "https://leetcode.com/accounts/login/"

def sign_in():
    driver.get(leetcode_login_link)
    driver.find_element(By.NAME, "login").send_keys(gmail)
    driver.find_element(By.NAME, "password").send_keys(pswd)
    driver.find_element(By.ID, "signin_btn").click()


def wait():
    a = input()

if __name__ == "__main__":
    sign_in()
    wait()
