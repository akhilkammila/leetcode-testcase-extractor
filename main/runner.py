
from problem_solver import ProblemSolver
from debug_wrapper import DebugWrapper

def solveProblem(problem_link, filePath):
    problemSolver = ProblemSolver(problem_link, filePath)
    problemSolver = DebugWrapper(problemSolver)

    problemSolver.login()
    problemSolver.load_problem()
    problemSolver.switch_to_python()
    problemSolver.reset_to_default()

    problemSolver.parse_inputs()
    problemSolver.setup_file()
    problemSolver.add_testcase()
    problemSolver.submit()

    while (not problemSolver.isSolved()):
        problemSolver.parse_testcase()
        problemSolver.add_testcase()
        problemSolver.submit()

if __name__ == "__main__":
    solveProblem("https://leetcode.com/problems/zigzag-conversion/", "6. Zigzag Conversion")