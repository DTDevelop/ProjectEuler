"""
Large sum
Problem 13
"""

import requests # retrieve html info
from bs4 import BeautifulSoup # parse html
import re # filter

def first_ten_digits(number):
    """
    given number
    returns first 10 digits of number
    """

    return first_ten

"""
QUESTIONS / SOLUTIONS
"""

# work out the first ten digits of the sum of the following one-hundred 50-digit numbers

url = "https://projecteuler.net/problem=13"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

# continue to parse with object methods

print('')
print('the first ten digits of the sum of one-hundred 50-digit numbers')
print(first_ten_digits(sum_of_numbers))
print('')
