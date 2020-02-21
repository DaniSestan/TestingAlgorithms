# Testing Algorithms in Python

## Description
**Status:** In Progress

This is a new, smaller project I've created for my own reference. Working on this to sharpen my Python skills by testing different algorithms ranging from simple to complex, and by measuring algorithmic efficiency.

---
### Proofs:
**Proof 01:** Induction on Loop Invariants for Merge Sort

**Proof 02:**

**Proof 03:**

**Proof 04:**

**Proof 05:**


### Exercises

**01_basic_algorithms:** simple program using binary search, basic performance timing, (deterministic) brute force algorithm, pure random algorithm

**02_algorithmic_efficiency:** testing understanding of algorithmic efficiency; solving algorithms with straightforward algebraic operations, as well as more complex manipulations, such as the the Lambert _W_ function, Stirling's Approximation, through convergence, etc. End result is printed to html file, displaying a table that returns comparisons of running times.

Problem: For each function _f(n)_ and the time _t_, evaluate the largest size n of problem that can be solved in time _t_, assuming that the algorithm to solve the problem takes _f(n)_ microseconds.

Functions _f(n)_: log<sub>2</sub>_n_, √_n_, _n_, _n_ log<sub>2</sub> _n_, _n_<sup>2</sup>, _n_<sup>3</sup>, 2<sup>_n_</sup>, and _n_!

Time periods: 1 second, 1 minute, 1 hour, 1 day, 1 month, 1 year, 1 century

**03_alg_effcy_merge**: Computing and displaying total number of comparisons to complete merge sorting algorithm, and time efficiency.

**04_alg_effcy_insertion**: Computing and displaying total number of comparisons to complete merge sorting algorithm, and time efficiency.

NOTE: LONG RUNNING PROGRAM. Provided test data will run for approx. ~20 hrs.

Run time for insertion sort with 1,000,000 integers will cap at over half a day. This makes it difficult to complete the sorting  algorithm to the end on a personal computer.  Below is just a suggestion for running this script.

1). On a Unix  (Linux) server,  copy the program.

2).  Add the following line at the very first line of the program and save the file.  This basically tells the Unix OS to run /user/bin/python3  with the Python script (program) in the file.  "#!" in this line of code is called  "shebang"  ('sh'  [Unix Bourne shell]  + bang , or hash + bang)

      #!/usr/bin/python3

3).  On the command line, at input prompt, enter the following Unix command to make the file (say "insertionSort.py")  executable.

      $ chmod +x insertionSort.py

4). Run the following command from the command line to run the code in background.

      $   nohup insertionSort.py  > sort.txt &

       This will run "insertionSort.py" in background by adding "&" at the end of command line.   Also the output of the command will be redirected  to and stored in sort.txt file instead of displaying on the display.   "nohup" at the beginning of the command line tells  Unix OS to continue to execute the command at the background even if the current login shell ends (which means you log out from the shell and terminates your putty session).



**04:**

**05:**

**06:**

**07:**

**08:**

**09:**

**10:**

**11:**

**12:**

**13:**

**14:**

**15:**

**16:**

**17:**

**18:**

**19:**

**20:**

**21:**

**22:**

**23:**

**24:**

**25:**

**26:**

**27:**

**28:**

**29:**

**30:**