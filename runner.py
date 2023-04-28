import pyperclip
from main_page_scraper import MainPageScraper
from problem_solver import ProblemSolver

def solveProblem(problem_link, filePath):
    problemSolver = ProblemSolver(problem_link, filePath)
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

def test():
    f = open("data/1.Two Sum", "a+")
    f.write('\n' + " "*8 + "hi")
    f.seek(0)
    pyperclip.copy(f.read())
    pyperclip.paste()

if __name__ == "__main__":
    # test()
    solveProblem("https://leetcode.com/problems/two-sum/", "data/1.Two Sum")