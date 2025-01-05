Arithmetic Formatter
A Python program that formats arithmetic problems vertically for better readability.

Description
This program takes arithmetic problems written horizontally and arranges them vertically following standard arithmetic formatting rules. For example:

32 3801 45

- 698 - 2 + 43

---

Usage

from main import arithmetic_arranger

# Basic usage

problems = ["32 + 698", "3801 - 2", "45 + 43"]
print(arithmetic_arranger(problems))

# With answers displayed

print(arithmetic_arranger(problems, True))

Function Reference

Parameters:
problems: List of strings containing arithmetic problems
show_answers: Boolean to display calculation results (default: False)
Returns: Formatted string of arranged problems

Rules and Limitations
The function accepts a maximum of 5 problems
The function only accepts addition and subtraction operations
Numbers cannot be more than 4 digits in length
Only digits are allowed (no letters or special characters)

Error Messages
The function will return:
"Error: Too many problems." if more than 5 problems are provided
"Error: Operator must be '+' or '-'." if an invalid operator is used
"Error: Numbers must only contain digits." if letters are used
"Error: Numbers cannot be more than four digits." if numbers are too large

Example Output
32 3801 45

- 698 - 2 + 43

---

730 3799 88 # (when show_answers=True)

Dependencies
Python 3.x
re (Regular Expression) module

Files
main.py: Contains the main implementation
