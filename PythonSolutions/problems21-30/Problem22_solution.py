"""
Names scores
Problem 22
"""

# CONSTANTS

MY_FILE = 'p022_names.txt'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_DICT = {}
for ind, letter in enumerate(alphabet):
    ALPHABET_DICT[letter] = ind+1


# HELPER FUNCTIONS

def file_name_split(my_file):
    """
    given (str) file path
    opens -> reads -> place each name into ordered array
    returns sorted array
    """
    name_array = []
    with open(my_file) as file:
        for line in file:
            split_line = line.split(',') # splits each name with specified delimiter
            name_array.extend(split_line) # into array
    name_array.sort()
    return name_array

def letter_value(letter):
    """
    for given (str) letter
    return (int) score
    """

    return ALPHABET_DICT[letter]

def name_total_value(name, index):
    """
    given (str) name and (int) index
    returns (int) score
    """
    name_score = 0
    for letter in name:
        name_score += letter_value(letter)

    return (name_score * index)

# test case
# we know, COLIN would obtain a score of 938 x 53 = 49714
print(name_total_value('COLIN', 938))

# expected output:
# 49714
# actual output:
# 49714

# MAIN FUNCTIONS

def solution():
    """
    solves and prints solution to P22
    returns None
    """
    names = file_name_split(MY_FILE)

    total_score = 0
    for ind, name in enumerate(names):
        score = name_total_value(name[1:-1], ind+1) # without ("")
        total_score += score

    print('')
    print('total of all the name scores in names.txt file')
    print(total_score)
    print('')

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

solution()


"""
notes
"""

# open file in same directory, read per line, split each w/ specified delimiter (',')
# sort file by alphabetical order
# remove "" from strings
