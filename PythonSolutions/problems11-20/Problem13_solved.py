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
    returns first 10 digits of number as int
    """
    first_ten = str(number)[:10]

    return int(first_ten)

"""
QUESTIONS / SOLUTIONS
"""

# work out the first ten digits of the sum of the following one-hundred 50-digit numbers

url = "https://projecteuler.net/problem=13"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

body = soup.find('body')
div = body.find('div', { 'class': 'monospace'})

sum_of_numbers = 0
my_numbers = [int(number) for number in div.text.split()]
for number in my_numbers:
    sum_of_numbers += number
# div.text  - retrieves contents without tags, returns as string
# .split()  - places elements within list, separating via whitespace
# list comprehension, applying to each element in list, convert to int

print('')
print('the first ten digits of the sum of one-hundred 50-digit numbers')
print(first_ten_digits(sum_of_numbers))
print('')
