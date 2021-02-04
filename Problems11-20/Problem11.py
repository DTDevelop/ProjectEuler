"""
Largest product in a grid
Problem 11
"""

# HELPER FUNCTIONS

def greatest_product_of_column(matrix, adjacent):
    """
    given matrix and number of adjacent
    return greatest product of column
    """
    greatest_product = 0

    matrix_length = len(matrix)

    for row in range(matrix_length):
        for num in range(matrix_length): # relative number to compare
            if num + adjacent > matrix_length: # not enough values in direction to compare
                break # move to next column
            new_product = 1
            for inc in range(adjacent): # calculating product
                new_product *= matrix[num+inc][row]
            if new_product > greatest_product:
                greatest_product = new_product

    return greatest_product

# test case

# test_matrix = [[1, 2, 3, 4, 5, 6, 7, 8]]*8
# test_matrix_2 = [[8,5,3,6],[5,9,3,2],[9,9,9,9],[1,2,9,9]]

# print(greatest_product_of_column(test_matrix,4))
# print(greatest_product_of_column(test_matrix_2,4))

# expected output:
# 4096 (8*8*8*8)
# 972 (9*9*2*6)

# actual output:
# 4096
# 972

def greatest_product_of_row(matrix, adjacent):
    """
    given matrix and number of adjacent
    return greatest product of row
    """
    greatest_product = 0

    matrix_length = len(matrix)

    for col in range(matrix_length):
        for num in range(matrix_length): # relative number to compare
            if num + adjacent > matrix_length: # not enough values in direction to compare
                break # move to next row
            new_product = 1
            for inc in range(adjacent): # calculating product
                new_product *= matrix[col][num+inc]
            if new_product > greatest_product:
                greatest_product = new_product
    return greatest_product

# test case

# test_matrix = [[1, 2, 3, 4, 5], [5, 6, 6, 6, 6], [7, 9, 9, 9, 9], [8, 9, 9, 3, 2], [2, 5, 7, 1, 9]]
# test_matrix_2 = [[8,5,3,6],[5,9,3,2],[1,9,2,9],[1,2,9,9]]

# print(greatest_product_of_row(test_matrix,4))
# print(greatest_product_of_row(test_matrix_2,4))

# expected output:
# 6561 (9*9*9*9)
# 720 (8*5*3*6)

# actual output:
# 6561
# 720

def greatest_product_of_diag(matrix, adjacent):
    """
    given matrix and number of adjacent
    return greatest product of diagonal
    """
    greatest_product = 0

    matrix_length = len(matrix)

    for col in range(matrix_length):
        for num in range(matrix_length): # relative number to compare
            if num + adjacent > matrix_length: # not enough values in direction to compare
                break # move to next row
            if col + adjacent > matrix_length: # not enough remaining diagonals to compare
                return greatest_product # end
            new_product = 1
            for inc in range(adjacent): # calculating product
                new_product *= matrix[col+inc][num+inc]
            if new_product > greatest_product:
                greatest_product = new_product
    return greatest_product

def greatest_product_of_rev_diag(matrix, adjacent):
    """
    given matrix and number of adjacent
    return greatest product of reverse diagonal
    """
    greatest_product = 0

    matrix_length = len(matrix)

    for col in range(matrix_length-1, -1, -1):
        for num in range(matrix_length-1, -1, -1): # relative number to compare
            if col + adjacent > matrix_length: # not enough numbers diagonal
                break # next row
            if num - adjacent < 0: # not enough numbers to the left
                break # next number
            new_product = 1
            for inc in range(adjacent): # calculating product
                new_product *= matrix[col+inc][num-inc]
            if new_product > greatest_product:
                greatest_product = new_product

    return greatest_product

# MAIN FUNCTION


def greatest_product(matrix, adjacent):
    """
    given matrix and number of adjacent
    return greatest product in same direction (up, down, left, right, diagonal)
    """

    # use and compare helper functions
    col = greatest_product_of_column(matrix, adjacent)
    row = greatest_product_of_row(matrix, adjacent)
    diag = greatest_product_of_diag(matrix, adjacent)
    rev_diag = greatest_product_of_rev_diag(matrix, adjacent)

    return max(col, row, diag, rev_diag) # returns highest product


# TEST FUNCTIONS
"""
the following are for manual testing
checking each output / pairing to ensure all values are covered
"""

def greatest_product_of_column_test(matrix, adjacent):
    """
    TEST FUNCTION: outputs each multiplication pairing
    given matrix and number of adjacent
    return greatest product of column
    """
    greatest_product = 0

    matrix_length = len(matrix)

    for row in range(matrix_length):
        print('col number: ', col) # CHECK
        for num in range(matrix_length): # relative number to compare
            if num + adjacent > matrix_length: # not enough values in direction to compare
                break # move to next column
            new_product = 1
            group_multiply = [] # CHECK
            for inc in range(adjacent): # calculating product
                new_product *= matrix[num+inc][row]
                group_multiply.append(matrix[num+inc][row]) # CHECK
            print(group_multiply) # CHECK
            if new_product > greatest_product:
                greatest_product = new_product
        print('') # CHECK

    return greatest_product

# expected output: all pairings up & down, length of adjacent
# acutal output: all pairings up & down, length of adjacent

def greatest_product_of_row_test(matrix, adjacent):
    """
    TEST FUNCTION: outputs each multiplcation pairing
    given matrix and number of adjacent
    return greatest product of row
    """
    greatest_product = 0

    matrix_length = len(matrix)

    for col in range(matrix_length):
        print('row number: ', col) # CHECK
        for num in range(matrix_length): # relative number to compare
            if num + adjacent > matrix_length: # not enough values in direction to compare
                break # move to next row
            new_product = 1
            group_multiply = [] # CHECK
            for inc in range(adjacent): # calculating product
                new_product *= matrix[col][num+inc]
                group_multiply.append(matrix[col][num+inc]) # CHECK
            print(group_multiply) # CHECK
            if new_product > greatest_product:
                greatest_product = new_product
        print('') # CHECK
    return greatest_product

# expected output: all pairings left & right, length of adjacent
# actual output: all pairings left & right, length of adjacent

def greatest_product_of_diag_test(matrix, adjacent):
    """
    TEST FUNCTION: outputs each multiplcation pairing
    given matrix and number of adjacent
    return greatest product of diagonal
    """
    greatest_product = 0

    matrix_length = len(matrix)

    for col in range(matrix_length):
        print('row number: ', col) # CHECK
        for num in range(matrix_length): # relative number to compare
            if num + adjacent > matrix_length: # not enough values in direction to compare
                break # move to next row
            if col + adjacent > matrix_length: # not enough remaining diagonals to compare
                return greatest_product # end
            new_product = 1
            group_multiply = [] # CHECK
            for inc in range(adjacent): # calculating product
                new_product *= matrix[col+inc][num+inc]
                group_multiply.append(matrix[col+inc][num+inc]) # CHECK
            print(group_multiply) # CHECK
            if new_product > greatest_product:
                greatest_product = new_product
        print('') # CHECK
    return greatest_product

# expected output: all pairings diagonally, length of adjacent
# actual output: all pairings diagonally, length of adjacent

def greatest_product_of_rev_diag_test(matrix, adjacent):
    """
    TEST FUNCTION: outputs each multiplication pairing
    given matrix and number of adjacent
    return greatest product of reverse diagonal
    """
    greatest_product = 0

    matrix_length = len(matrix)

    for col in range(matrix_length-1, -1, -1):
        print('row number: ', col) # CHECK
        for num in range(matrix_length-1, -1, -1): # relative number to compare
            if col + adjacent > matrix_length: # not enough numbers diagonal
                break # next row
            if num - adjacent < 0: # not enough numbers to the left
                break # next number
            new_product = 1
            group_multiply = [] # CHECK
            for inc in range(adjacent): # calculating product
                new_product *= matrix[col+inc][num-inc] # next column, earlier index
                group_multiply.append(matrix[col+inc][num-inc]) # CHECK
            print(group_multiply) # CHECK
            if new_product > greatest_product:
                greatest_product = new_product
        print('') # CHECK

    return greatest_product

# expected output: all pairings reverse_diagonally, length of adjacent
# actual output: all pairings reverse_diagonally, length of adjacent

"""
QUESTIONS / SOLUTIONS
"""

# iin the 20x20 grid, four numbers along a diagonal line have been marked

# the product of these numbers is 26 * 63 * 78 * 14 = 1788696

grid = '\
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

# grid input as string
# separate each value via white space & place into list of list
# creating a 20x20 matrix

my_numbers = grid.split()
number_matrix = []
for dummy_i in range(20):
    new_list = []
    for num in my_numbers[:20]:
        new_list.append(num)
    number_matrix.append(new_list)
    my_numbers = my_numbers[20:] # trim

number_matrix = [[int(num) for num in group] for group in number_matrix] # list comprehension convert strings to int

# test function outputs
# print(greatest_product_of_row_test(number_matrix, 4))
# print(greatest_product_of_column_test(number_matrix, 4))
# print(greatest_product_of_diag_test(number_matrix, 4))
# print(greatest_product_of_rev_diag_test(number_matrix, 4))

# what is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, diagonal)
# in the 20x20 grid?

print('\n')
print('what is the greatest product of four adjacent numbers in the same direction')
print(greatest_product(number_matrix, 4))
