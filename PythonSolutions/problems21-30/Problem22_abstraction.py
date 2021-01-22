"""
Names scores
Problem 22
"""

# CONSTANTS

my_file = ''

# HELPER FUNCTIONS

def file_name_split(my_file):
    """
    given (str) file path
    opens -> reads -> place each name into ordered array
    returns array
    """
    with open(my_file) as file:
        for line in file:
            pass

    return name_array

def letter_value(letter):
    """
    for given (str) letter
    return (int) score
    """

    return score

def name_total_value(name, index):
    """
    given (str) name and (int) index
    returns (int) score
    """

    return score

# MAIN FUNCTIONS

def solution():
    """
    solves and prints solution to P22
    returns None
    """

    return

"""
QUESTIONS / SOLUTIONS
"""

# using names.txt, 46k text file containing over five-thousand first names, begin by sorting
# into alphabetical order. working out alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score

# For example, list is sorted into alphabetical order, COLIN, which is worth
# 3 + 15 + 12 + 9 + 14 = 53, 938th name in the list
# COLIN woudl obtain a score of 938 * 53 = 49714

# total of all the name scores in the file?


"""
notes
"""

# open file in same directory, read per line, split each w/ specified delimiter
