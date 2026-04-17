#!/usr/bin/env python3

# getbest.py
# Finds the top student in a class based on marks provided in a CSV file.

# Assumptions based on lab specifications --->

# ------------->> 1. All marks are unique.
# ------------->> 2. Two of the headings will be "Student Number" and "Mark".
# ------------->> 3. The order of the columns can possibly differ between files.
# ------------->> 4. All data files are in the correct, readable CSV format.

import sys

def getCols(f):
    # Identify the columns that contain the marks and student numbers dynamically. 

    headings = f.readline().strip().split(",")
    
    # Iterate through all headings using range(len()) to handle any column order
    
    for i in range(len(headings)):
        if headings[i] == "Student Number":
            num_col = i
        elif headings[i] == "Mark":
            mark_col = i
            
    return (num_col, mark_col)


def findTop(f, num_col, mark_col):
    
    # Scans the file to find and return the top student in the class.

    best = 0
    best_idx = 0
    
    # Loop through the remaining data rows
    
    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])
        
        # Fixed a bug now updates both the highest mark and the corresponding student number
        if mark > best:
            best = mark
            best_idx = data[num_col]
            
    return best_idx, best


def get_best_student(filename):
    
    # Wrapper function to facilitate unit testing and isolate logic from sys.argv.
    
    # Professional Practice improvement now uses 'with open' to ensure the file is closed automatically
    
    with open(filename, 'r') as f:
        num_col, mark_col = getCols(f)
        best_idx, best = findTop(f, num_col, mark_col)
        
    return best_idx, best


if __name__ == "__main__":

    # Extract filename from command line arguments and execute

    student, mark = get_best_student(sys.argv[1])
    print("The top student was student %s with %d" % (student, mark))