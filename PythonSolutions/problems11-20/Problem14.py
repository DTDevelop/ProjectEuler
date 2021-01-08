"""
Longest Collatz sequence
Problem 14
"""


"""
QUESTIONS / SOLUTIONS
"""

# the following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# using the rule above and starting with 13, we generate the following sequence:
# 13 - 40 - 20 - 10 - 5 = 16 = 8 = 4 = 2 = 1

# can be seen that this sequence contains 10 terms
# although not proven, it is thought that all starting numbers finish at 1

# which starting number, under one million, produces the longest chain?
# NOTE: Once chain starts the terms are allowed to go above one million
