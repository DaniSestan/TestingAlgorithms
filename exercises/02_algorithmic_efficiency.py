# Program Plan:

# Try referencing the 'Comparison of Running Times' problem.
# Consider using 'scipy', 'numpy', 'math', or any other modules to solve this.
# The output will be in a HTML text format which includes a table with the responses. Use any HTML library module or simple print() or write() functions to write my html file. When the file is loaded on a browser, it should display a table in a reasonably nice table format looking like the one in the textbook.

# For each function f(n) and time t in the following table,
# determine the largest size n of a problem that can be solved in time t,
# assuming that the algorithm to solve the problem takes f(n) microseconds.

#               1 SECOND | 1 MINUTE |   1 HOUR  |   1 DAY   |  1 MONTH  |   1 YEAR  | 1 CENTURY
#             __________________________________________________________________________________
#   lg n      ___________|__________|___________|___________|___________|___________|___________
#   sqrt(n)   ___________|__________|___________|___________|___________|___________|___________
#   n         ___________|__________|___________|___________|___________|___________|___________
#   n lg n    ___________|__________|___________|___________|___________|___________|___________
#   n2        ___________|__________|___________|___________|___________|___________|___________
#   n3        ___________|__________|___________|___________|___________|___________|___________
#   2n        ___________|__________|___________|___________|___________|___________|___________
#   n!        ___________|__________|___________|___________|___________|___________|___________

from tabulate import tabulate
import os
import webbrowser
import math
import decimal
from decimal import Decimal


def comparisonOfRunningTimes():
    # defining the table headers and the initial table values as column (at index 0) with values for function 'f(n)'
    #  each list contained in the table corresponds to a row that will be appended with
    #  time values for each each function f(n)
    headers = ["f(n)", "1 second", "1 minute", "1 hour", "1 day", "1 month", "1 year", "1 century"]
    table = [["lg n"], ["&#8730;n"], ["n"], ["n lg n"], ["n<sup>2</sup>"], ["n<sup>3</sup>"], ["2<sup>n</sup>"],
             ["n!"]]

    # included a dictionary of values for my own reference of time conversions:
    #  The number of days in a year is assumed to be 356. The number of days in a month is assumed to be 30.
    #  Based on these values, the AVERAGE number of years is calculated as '365/30' or '12.16666667'
    times = {"1 second in nanoseconds": 10 ** 6, "1 minute in seconds": 60, "1 hour in minutes": 60,
             "1 day in hours": 24, "1 month in days": 30, "1 year (356 days) in avg months": 365/30,
             "1 century in years": 100}

    # values to be used in calculating table results
    conversions = list(times.values())

    # inner function: called for each function f(n) (indicated with 2 arguments:
    #  arg 1: index of row (as index value of outer 'table' list
    #  arg 2: - this function is called inside nested for loop; is called for each column ('k')
    #         - the function used/called should correspond to the type of function f(n) in the table

    def solveForN(row, function):
        j = 0
        while j < len(times):
            result = 1
            for k in range(j+1):
                result = result * (conversions[k])
            table[row].append(function(result))
            j += 1

    # inner function: solve for exponent in decimal equivalent of time
    def fexp(number):
        (sign, digits, exponent) = Decimal(number).as_tuple()
        return len(digits) + exponent - 1

    # inner function: solve for mantissa in decimal equivalent of time
    def fman(number):
        return Decimal(number).scaleb(-fexp(number)).normalize()

    # TODO: write function to combine process for (at least first three) functions,
    #  which should take into account log base, and any exponents of n to be used as a
    #  factor of the 'exponent' variable

    # inner function: lg n
    def operationForLogN(t):
        exponent = fexp(t)
        mantissa = fman(t)
        # if-else statement to simplify printed values, such as 2^(10^6) versus 2^(1 * 10^6)
        if mantissa != 1:
            return "2<sup>%d x 10<sup>%d</sup></sup>" % (mantissa, exponent)
        else:
            return "2<sup>10<sup>%d</sup></sup>" % exponent

    # inner function: sqrt(n)
    def operationForSqrtOfN(t):
        exponent = fexp(t) * 2
        mantissa = fman(t) ** 2
        if mantissa != 1:
            return "%s x 10<sup>%s</sup>" % (str(mantissa), str(exponent))
        else:
            return "10<sup>%s</sup>" % str(exponent)

    # n
    def operationForN(t):
        exponent = fexp(t)
        mantissa = fman(t)
        if mantissa != 1:
            return "%s x 10<sup>%s</sup>" % (str(mantissa), str(exponent))
        else:
            return "10<sup>%s</sup>" % str(exponent)

    # n log n

    # n^2

    # n^3

    # 2^n

    # n!

    # test:
    solveForN(0, operationForLogN)
    solveForN(1, operationForSqrtOfN)
    solveForN(2, operationForN)

    message = """<html><head></head><body><h1>Comparison of Running Times</h1>""" + \
              tabulate(table, headers, tablefmt="html") \
              + """</body></html>"""

    f = open('Comparison of Running Times', 'w')
    f.write(message)
    f.close()

    webbrowser.open_new_tab('file://' + os.getcwd() + '/Comparison of Running Times')


comparisonOfRunningTimes()
