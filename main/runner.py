import sys
import os
import csv
from problem_solver import ProblemSolver
from debug_wrapper import DebugWrapper

def solveProblem(problem_link, filePath):
    problemSolver = ProblemSolver(problem_link, filePath)
    problemSolver = DebugWrapper(problemSolver)

    if (problemSolver.overCharacterLimit()):
        print("Already Solved", flush=True)
        return
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

def getRow(rowNumber):
    with open('problem_data/problem_data.csv', 'r') as file:
        csv_reader = csv.reader(file)

        # Convert the CSV reader object to a list of rows
        rows = list(csv_reader)[1:]

        return rows[rowNumber]

if __name__ == "__main__":
    arguments = sys.argv[1:]
    rowNumber = int(arguments[0])
    row = getRow(rowNumber)

    probNumber, probTitle, probLink = row[0], row[1], row[2]
    solveProblem(probLink, probNumber + ". " + probTitle)