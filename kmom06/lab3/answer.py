#!/usr/bin/env python3

"""
a932b324a109e933feb1a2daa557005e
oopython
lab3
v2
zowa22
2025-03-02 14:28:10
v4.0.0 (2019-03-05)

Generated 2025-03-02 15:28:10 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - Recursion
#
# If you need to peek at examples or just want to know more, take a look at
# the page: https://docs.python.org/3/library/index.html. Here you will find
# everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Simple recursion
#
# Practice on creating recursive functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers `13` up to `32`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#

def the_sum(start, end):
    """räknar summan av nummer mellan start och end"""
    total_sum = 0
    for number in range(start, end + 1):
        total_sum += number
    return total_sum



ANSWER = the_sum(13, 32)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create a recursive function in the code below that searches for the maximum
# element of a list and returns that number.
# Find the maximum value in the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
#
# Answer with the maximumx value.
#
# Write your code below and put the answer into the variable ANSWER.
#

def find_max(lst):
    """hittar max tall"""
    if len(lst) == 1:
        return lst[0]

    max_of_rest = find_max(lst[1:])

    if lst[0] > max_of_rest:
        return lst[0]
    return max_of_rest

numbers = [4, 5, 6, 11, 9, 1, 2, 3, 8]



ANSWER = find_max(numbers)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a recursive function in the code below that searches a list for a
# number and returns the index of the number.
# Find the index of `1` in the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
# If the number cant be found, return -1.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#
def find_index(lst, numret, index=0):
    """hittar spesifikt index"""
    if len(lst) == 0:
        return -1

    if lst[0] == numret:
        return index

    return find_index(lst[1:], numret, index + 1)

numbers = [4, 5, 6, 11, 9, 1, 2, 3, 8]

ANSWER = find_index(numbers, 1)
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Use the function from the previous assignment to find the number `10` in
# the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = find_index(numbers, 10)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a recursive function in the code below that calculates `10` to the
# power of `7`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

def power_of_ten(exponent):
    """beräknar till kraften av 10"""
    if exponent == 0:
        return 1
    return 10 * power_of_ten(exponent - 1)




ANSWER = power_of_ten(7)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a recursive function in the code below that turns a string
# backwards. Turn the string "Backwards" backwards.
#
# Answer with the backward string.
#
# Write your code below and put the answer into the variable ANSWER.
#
def reverse_str(s):
    """skriver sträng baklänges """
    if len(s) == 0:
        return s
    return s[-1] + reverse_str(s[:-1])

ANSWER = reverse_str("Backwards")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a recursive function in the code below that calculates the "lowest
# common multiple" between two numbers.
# It should return the smallest positive integer that is divisible by both
# "9" and "5".
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
def berakna_gcd(tal1, tal2):
    """beräknar gretest common multiple"""
    if tal2 == 0:
        return tal1
    return berakna_gcd(tal2, tal1 % tal2)

def berakna_lcm(tal1, tal2):
    """beräknar lowest common multiple"""
    return (tal1 * tal2) // berakna_gcd(tal1, tal2)


ANSWER = berakna_lcm(9, 5)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)


dbwebb.exit_with_summary()
