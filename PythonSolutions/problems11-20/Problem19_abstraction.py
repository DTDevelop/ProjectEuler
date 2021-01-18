"""
Counting sundays
Problem 19
"""


"""
QUESTIONS / SOLUTIONS
"""

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# how many sundays fell on the first month during the twentieth century
# 1 Jan 1901 to 31 Dec 2000

"""
NOTES
"""

# as values don't need to be stored, cycle up to day / time required
# start reference
# day: Jan 1, 1900 == Monday


# # # KEEP TRACK OF

# current_year = 1900
# max_year = 2000

# current_month = 1 (increments)
# max_month = 12

# current_day = 1 (increments)
# max_day = vary on month + leap year

# day_name = 1 (increments)
# day_name_max = 7 (days of the week)


# # # DETERMINE LEAP YEAR

# if month == 4, 6, 9, 11: set max_day = 30 ( for select months )

# if month == 2 (february)
#   if current_year % 4 == 0: set max_day = 29 ( leap year )
#   else: set max_day == 28

# else: set max_day = 31 ( rest of the months )
