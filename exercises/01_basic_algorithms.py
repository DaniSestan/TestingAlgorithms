# Testing the following:
# - binary search
# - basic performance timing
# - measure performance of (deterministic) brute force algorithm versus pure random algorithm

import time
import random

# common number guessing game, with the typical roles reversed
# -- rather than prompting the user to guess the number, the user will
# choose a number and evaluate the program's guesses as lower/higher/correct.
def guessing_game():
    num = 0
    response = ''
    i = 0
    low_num = 1
    high_num = 1000

    while num < 1 or num > 1000:
        # try-catch to validate the input as an int
        try:
            num = int(input("Enter a number between 1 and 1000:"))
        except ValueError:
            print("Invalid input. Try again.")

    while response != 'c':
        i += 1
        guess_num = (low_num + high_num) // 2
        print("Computer guesses: ", guess_num)
        while True:
            response = input("Type 'l' if larger, 's' if smaller, 'c' if correct: ")
            if response == 'l':
                low_num = guess_num + 1
                break
            elif response == 's':
                high_num = guess_num
                break
            elif response == 'c':
                break
            else:
                print("Invalid input. Try again.")

    print("Done! Your number is %d. Guessed in %d time(s)" % (num, i))


# The following decorator is to be used for passing functions w/their own parameters as argumentss
# in another function. Test with the time_efficiency function.
def wrap_function(func, *args, **kwargs):
    def wrap():
        return func(*args, **kwargs)

    return wrap


# def time_efficiency(func, *args, **kwargs):
def time_efficiency(func):
    start = time.perf_counter_ns() / 10**9
    # func(*args, **kwargs)
    func()
    end = time.perf_counter_ns() / 10**9
    duration = end - start

    print("Starts at: ", start)
    print("Ends at: ", end)
    print("Time taken to execute the function: %f seconds" % duration)

    return duration


def sum_up():
    num = 0
    sum_num = 0
    while num <= 0:
        try:
            num = int(input("Enter your_num for 0 .. your_num: "))
        except ValueError:
            print("Invalid input. Try again")

    while num >= 0:
        sum_num += num
        num -= 1

    return sum_num


# function for testing decorator
def foo(n):
    print("printing from function to test decorator")


# testing decorator
# TODO: remove commenting on two lines below
wrapped_func = wrap_function(foo, 'bar')
time_efficiency(wrapped_func)


def another_guessing_game(guess_method):
    highest_tries = 0
    lowest_tries = 0
    correct_tries = 0
    total_tries = 0
    reached_upperbound_occurrences = 0

    for number_of_tries in range(0, 10000):
        random_nums = random.sample(range(0, 10), 3)
        result = guess_method(random_nums)
        if result[0] == random_nums:
            correct_tries += 1
        if highest_tries < result[1]:
            highest_tries = result[1]
        if lowest_tries > result[1] or lowest_tries == 0:
            lowest_tries = result[1]
        if result[1] > 10000:
            reached_upperbound_occurrences += 1
        total_tries += result[1]

    print("Number of tries: ", correct_tries)
    print("Highest number of guesses in a try: ", highest_tries)
    print("Lowest tries: ", lowest_tries)
    print("Number of correct tries: ", correct_tries)
    print("Average number of tries: ", total_tries / number_of_tries)
    if reached_upperbound_occurrences > 0:
        print("Reached upper-bound limit %d times" % reached_upperbound_occurrences)


def deterministic_brute_force_guessing(nums):
    random_nums = int(''.join(map(str, nums)))
    guess = 0

    while guess != random_nums and guess < 10000:
        guess += 1

    result = list(map(int, str(guess)))
    while len(result) < 3:
        result.insert(0, 0)

    return [result, guess]


def pure_random_guessing(nums):
    guess = 0
    i = 0

    for i in range(0, 10000):
        if guess != nums:
            guess = random.sample(range(0, 10), 3)
        else:
            break

    return [guess, i]


def top_word_occurrences():
    file = input("Enter file path: ")
    n = int(input("Enter the number of most frequent words to display: "))
    word_dict = {}

    with open(file) as f:
        word_list = [word for line in f for word in line.split()]

    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1

    for i in range(n):
        print('%s : %d' % (sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[i][0], sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[i][1]))


guessing_game()
time_efficiency(sum_up)
another_guessing_game(deterministic_brute_force_guessing)
another_guessing_game(pure_random_guessing)
top_word_occurrences()
