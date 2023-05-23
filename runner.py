from problem_solver import ProblemSolver
import time

def solveProblem(problem_link, filePath):
    try:
        problemSolver = ProblemSolver(problem_link, filePath)
        problemSolver.login()
        problemSolver.bypass_catpcha()
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
        problemSolver.screenshot("error.png")
        time.sleep(100)

if __name__ == "__main__":
    solveProblem("https://leetcode.com/problems/sudoku-solver/", "data/37. Sudoku Solver")