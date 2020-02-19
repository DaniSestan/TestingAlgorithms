# Program Plan:

# Try referencing the 'Comparison of Running Times' problem.
# Consider using 'scipy', 'numpy', 'math', or any other modules to solve this.
# The output will be in a HTML text format which includes a table with the responses. Use any HTML library module or simple print() or write() functions to write my html file. When the file is loaded on a browser, it should display a table in a reasonably nice table format looking like the one in the textbook.

# For each function f(n) and time t in the following table,
# determine the largest size n of a problem that can be solved in time t,
# assuming that the algorithm to solve the problem takes f(n) microseconds.

#               1 SECOND | 1 MINUTE |   1 HOUR  |   1 DAY   |  1 MONTH  |   1 YEAR  | 1 CENTURY

#   lg n      ___________|__________|___________|___________|___________|___________|___________
#   √n        ___________|__________|___________|___________|___________|___________|___________
#   n         ___________|__________|___________|___________|___________|___________|___________
#   n lg n    ___________|__________|___________|___________|___________|___________|___________
#   n2        ___________|__________|___________|___________|___________|___________|___________
#   n3        ___________|__________|___________|___________|___________|___________|___________
#   2n        ___________|__________|___________|___________|___________|___________|___________
#   n!        ___________|__________|___________|___________|___________|___________|___________

from tabulate import tabulate
import os
import webbrowser
import sys
from decimal import Decimal
import math


def comparison_of_running_times():
    # defining the table headers and the initial table values as column (at index 0) with values for function 'f(n)'
    #  each list contained in the table corresponds to a row that will be appended with
    #  time values for each each function f(n)
    headers = ["f(n)", "1 second", "1 minute", "1 hour", "1 day", "1 month", "1 year", "1 century"]
    table = [["lg n"], ["√n"], ["n"], ["n lg n"], ["n<sup>2</sup>"], ["n<sup>3</sup>"], ["2<sup>n</sup>"],
             ["n!"]]

    # included a dictionary of values for my own reference of time conversions:
    #  The number of days in a year is assumed to be 356. The number of days in a month is assumed to be 30.
    #  Based on these values, the AVERAGE number of years is calculated as '365/30' or '12.16666667'
    times = {
        "1 second in nanoseconds": 10 ** 6,
        "1 minute in seconds": 60, "1 hour in minutes": 60,
        "1 day in hours": 24,
        "1 month in days": 30,
        "1 year (356 days) in avg months": 365/30,
        "1 century in years": 100
    }

    # values to be used in calculating table results
    conversions = list(times.values())

    # inner function: called for each function f(n) (indicated with 2 arguments:
    #  arg 1: index of row (as index value of outer 'table' list
    #  arg 2:   - this function is called inside nested for loop; is called for each column ('k')
    #           - the function used/called should correspond to the type of function f(n) in the table
    #  **args:  - the values to be used as arguments in the callback function (second argument)
    def solve_time_for_f_of_n(row, function, *args):
        j = 0
        while j < len(times):
            result = 1
            for k in range(j+1):
                result = result * (conversions[k])
            table[row].append(function(result, *args))
            j += 1

    # inner function: solve for exponent in decimal equivalent of time
    def fexp(number):
        (sign, digits, exponent) = Decimal(number).as_tuple()
        return len(digits) + exponent - 1

    # inner function: solve for mantissa in decimal equivalent of time
    def fman(number):
        return Decimal(number).scaleb(-fexp(number)).normalize()

    # inner function: used for operation in f(n) = lg n, √n, or n; returns result in Scientific notation
    def eval_time_sci_notation(t, exp, base=''):
        exponent = fexp(t) * exp
        mantissa= fman(t) ** exp

        if mantissa != 1:
            result = "%s x 10<sup>%s</sup>" % (str(mantissa), str(exponent))
        else:
            result = "10<sup>%s</sup>" % str(exponent)

        if base == 2:
            return "2<sup>%s</sup>" % result

        return result

    # inner function: used for operation in f(n) = n log n
    #  This function uses n = time/log2(n) and then does a fixed point iteration, starting with n0 = t.
    #  The resulting values are asymptotic -- n and t/math(log(n,2) become exponentially closer to a 1:1 ratio.
    #  Once the boundary is approached, n is returned from the function. The breaking condition can be reached
    #  by rounding the result of t / math.log(n,2).
    def eval_time_for_n_log_n(t):
        n = t
        while round(t / math.log(n, 2)) != n:
            n = round(t / math.log(n, 2))

        return n

    # inner function: used for operation in f(n) = n^2 or n^3; returns result in integer notation
    def eval_time_int_notation(result, root):
        root = 1/root
        return round(math.pow(result, root))

    # inner function: used for operation in f(n) = 2^n
    def eval_time_for_2_to_n(time):
        n = 1
        while math.pow(2, n) < time:
            n += 1
        return n - 1

    # inner function: used for operation in f(n) = n!
    def eval_time_for_n_factorial(time):
        n = 1
        while math.factorial(n) < time:
            n += 1
        return n - 1

    # print to table
    solve_time_for_f_of_n(0, eval_time_sci_notation, 1, 2)
    solve_time_for_f_of_n(1, eval_time_sci_notation, 2)
    solve_time_for_f_of_n(2, eval_time_sci_notation, 1)
    solve_time_for_f_of_n(3, eval_time_for_n_log_n)
    solve_time_for_f_of_n(4, eval_time_int_notation, 2)
    solve_time_for_f_of_n(5, eval_time_int_notation, 3)
    solve_time_for_f_of_n(6, eval_time_for_2_to_n)
    solve_time_for_f_of_n(7, eval_time_for_n_factorial)

    message = """<html><head></head><body><h1>Comparison of Running Times</h1>""" + \
              tabulate(table, headers, tablefmt="html") \
              + """</body></html>"""

    f = open('Comparison of Running Times', 'w')
    f.write(message)
    f.close()

    webbrowser.open_new_tab('file://' + os.getcwd() + '/Comparison of Running Times')


comparison_of_running_times()
