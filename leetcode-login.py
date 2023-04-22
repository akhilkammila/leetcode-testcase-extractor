import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #keeps window open after running for debugging
driver = webdriver.Chrome(options=options)

leetcode_link = "https://leetcode.com/"

def sign_in():
    driver.get(leetcode_link)

if __name__ == "__main__":
    sign_in()