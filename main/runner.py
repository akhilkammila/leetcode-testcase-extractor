from problem_solver import ProblemSolver
import time
from csv import DictReader

def solveProblem(problem_link, filePath):
    problemSolver = ProblemSolver(problem_link, filePath)
    problemSolver.login_with_cookies()
    time.sleep(1000)
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

def test():
    filename = "main/leetcode_cookies.csv"
    result = []
    with open(filename, 'r') as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            clean_row = {key.strip(): value.strip() for key, value in row.items() if key!=""}
            result.append(clean_row)
    print(result)

if __name__ == "__main__":
    solveProblem("https://leetcode.com/problems/sudoku-solver/", "data/37. Sudoku Solver")