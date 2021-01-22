"""
Amicable numbers
Problem 21
"""


"""
QUESTIONS / SOLUTIONS
"""

# let d(n) be defined as the sum of proper divisors of n
# ( numbersless than n which divide evenly into n )

# if d(a) = b and d(b) = a, where a != b, then a and b are an amicabl pair
# each of a and b are called amicable numbers

# eg.
# proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110
# therefore d(220) = 284
# proper divisors of 284 are 1, 2, 4, 71 and 142
# therefore d(284) = 220

# evaluate the sum of all the amicable numbers under 10000
