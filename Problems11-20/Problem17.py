"""
Number letter counts
Problem 17
"""

# NAME DICTIONARIES

ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tensplus = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

# HELPER FUNCTIONS

def letter_count(word):
    """
    given a word
    returns number of total letters used (removes dashes and spaces)
    """
    word.replace(' ', '')
    word.replace('-', '') # removes occurences of - and space

    return len(word)

def number_name_convert(number):
    """
    given number from 1 to 1000
    convert to name
    """
    name = ''
    current_number = number

    # NUMBER 1000 EXCLUSIVE
    if current_number == 1000:
        name = 'one thousand'
        print(name)
        return name

    # NUMBERS WITH 100 ELEMENT
    hundred_check = current_number / 100.0
    hundred_check_int = int(hundred_check)
    if hundred_check_int >= 1:
        name += ones[hundred_check_int]
        name += 'hundred'

        if current_number % 100 > 0: # if non 00 in tens and one places
            name += 'and'
            current_number -= (hundred_check_int*100) # trim 100s place
        else:
            return name

    # NUMBERS WITH TENS ELEMENT
    tens_check = current_number / 10.0 # int

    if tens_check >= 1:
        if tens_check < 2: # for 10 - 19
            name += tens[current_number]
            print(name)
            return name

        else: # for 20 - 99
            name += tensplus[int(tens_check)]

    # NUMBERS IN ONES ELEMENT
    ones_check = current_number % 10
    if ones_check > 0:
        name += ones[ones_check] # for ones element
    print(name)
    return name

# TEST CASE
# 6, 72, 138
# 15, 30, 200, 999, 1000
# test_case = [6, 15, 30, 72, 138, 200, 999, 1000]
#
# for number in test_case:
#     print(number_name_convert(number))

# expected output:
# six, fifteen, thirty, seventytwo, onehundredandthirtyeight, twohundred, ninehundredandninteynine, one thousand

# actual output:
# six
# fifteen
# thirty
# seventytwo
# onehundredandthirtyeight
# twohundred
# ninehundredandninetynine
# one thousand

# MAIN FUNCTIONS

def total_letters_in_range(start, end):
    """
    given starting value and ending value
    returns numbers of letters used in all names
    """
    count = 0
    current_number = start

    while current_number <= end:
        count += letter_count(number_name_convert(current_number))
        current_number += 1

    return count

"""
QUESTIONS / SOLUTIONS
"""

# TEST CASE
#
# if the numbers 1 to 5 are written out in words
# eg. one, two, three, four, five
# the letters used in total == 19
#
# print('\n')
# print(total_letters_in_range(1, 5))
#
# expected output:
# 19
#
# actual output:
# 19


# if all numbers from 1 to 1000 (one thousand) were written out in words
# how many letters would be used?

# spaces or hyphens do not count
# eg. 342, three hundred and forty two contains 23 letters
# eg. 115, one hundred and fifteen contains 20 letters
# the 'and' is used in compliance with british usage

# print('\n')
# print('if all nubmers from 1 to 1000 were written out in words, how many letters would be used')
print(total_letters_in_range(1, 1000))
