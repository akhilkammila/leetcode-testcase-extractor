import sys
import csv
from problem_solver import ProblemSolver
from debug_wrapper import DebugWrapper

def solveProblem(problem_link, filePath, firstTime = True):
    problemSolver = ProblemSolver(problem_link, filePath)
    problemSolver = DebugWrapper(problemSolver)

    problemSolver.login()
    problemSolver.load_problem()
    problemSolver.switch_to_python()
    problemSolver.reset_to_default()

    problemSolver.parse_inputs()
    if firstTime: problemSolver.setup_file()
    problemSolver.add_testcase()
    problemSolver.submit()

    while (not problemSolver.isSolved()):
        problemSolver.parse_testcase()
        problemSolver.add_testcase()
        problemSolver.submit()

def getRow(rowNumber):
    with open('data/problem_data.csv', 'r') as file:
        csv_reader = csv.reader(file)

        # Convert the CSV reader object to a list of rows
        rows = list(csv_reader)[1:]

        return rows[rowNumber]

if __name__ == "__main__":
    arguments = sys.argv[1:]
    rowNumber = int(arguments[0])
    firstTime = True
    if len(arguments) > 1 and arguments[1] == "False":
        firstTime = False
    row = getRow(rowNumber)

    probNumber, probTitle, probLink = row[0], row[1], row[2]
    solveProblem(probLink, probNumber + ". " + probTitle, firstTime)