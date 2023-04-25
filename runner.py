import time
from main_page_scraper import MainPageScraper
from problem_solver import ProblemSolver

def solveProblem(problem_link):
    problemSolver = ProblemSolver(problem_link)
    problemSolver.login()
    problemSolver.load_problem()
    problemSolver.switch_to_python()
    problemSolver.parse_inputs()
    problemSolver.add_testcase(default=True)
    problemSolver.submit()
    while (not problemSolver.isSolved()):
        problemSolver.parse_testcase()
        problemSolver.add_testcase()
        problemSolver.submit()
    problemSolver.manual_wait()

if __name__ == "__main__":
    solveProblem("https://leetcode.com/problems/two-sum/")