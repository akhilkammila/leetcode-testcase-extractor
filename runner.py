import pyperclip
from main_page_scraper import MainPageScraper
from problem_solver import ProblemSolver

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

def solveProblem(problem_link, filePath):
    problemSolver = ProblemSolver(problem_link, filePath)
    problemSolver.login()
    problemSolver.load_problem()
    problemSolver.switch_to_python()

    problemSolver.parse_inputs()
    problemSolver.setup_file()
    problemSolver.add_testcase()
    problemSolver.submit()

    while (not problemSolver.isSolved()):
        problemSolver.parse_testcase()
        problemSolver.add_testcase()
        problemSolver.submit()
    problemSolver.manual_wait()

def test():
    "Initialize a remote webdriver"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=chrome_options
    )

if __name__ == "__main__":
    solveProblem("https://leetcode.com/problems/sudoku-solver/", "data/37. Sudoku Solver")