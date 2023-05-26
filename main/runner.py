import time
from problem_solver import ProblemSolver
from debug_wrapper import DebugWrapper
import traceback

def solveProblem(problem_link, filePath):
    try:
        problemSolver = ProblemSolver(problem_link, filePath)
        problemSolver = DebugWrapper(problemSolver)

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
    except:
        traceback.print_exc()
        problemSolver.screenshot("error.png")
        problemSolver.driver.quit()
        print("quit")

if __name__ == "__main__":
    solveProblem("https://leetcode.com/problems/zigzag-conversion/", "data/6.Zigzag Conversion")