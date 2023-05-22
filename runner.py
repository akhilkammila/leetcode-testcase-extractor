import pyperclip
from problem_solver import ProblemSolver
from login_bot import LoginBot

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

def login():
    login_bot = LoginBot()
    login_bot.google_login()
    login_bot.leetcode_login()

def solveProblem(problem_link, filePath):
    try:
        problemSolver = ProblemSolver(problem_link, filePath)
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
    except:
        problemSolver.screenshot("error.png")

if __name__ == "__main__":
    login()
    solveProblem("https://leetcode.com/problems/sudoku-solver/", "data/37. Sudoku Solver")