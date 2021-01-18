"""
Counting sundays
Problem 19
"""
days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
months = {'January': 0, 'February': 1, 'March': 2, 'April': 3, 'May': 4, 'June': 5, 'July': 6, 'August': 7, 'September': 8, 'October': 9, 'November': 10, 'December': 11}

# parameter KEY
# specified = day name wanted
# start_day = int, 1-31
# day_name = day of the week, str ('Monday', 'Tuesday', ...)
# start_month = month name str ('January', 'February', ...)
# start_year = int, eg. 1900, 1911, ...
# end_ .. similar as above

def number_of_days(specified, start_day, day_name, start_month, start_year, end_day, end_month, end_year):
    """
    enter valid starting date & ending date ( up to and including provided date time )
    returns number of days that fell on the first of the month from range
    """
    specified_day = days[specified]
    number_of_specified = 0

    current_day = start_day
    day_name = days[day_name]
    current_month = months[start_month]
    current_year = start_year

    max_day = None # set during month identification
    day_name_max = 6
    max_month = 12 # (months counted from 0 - 11)

    last_month = months[end_month]

    year_trigger = False
    month_trigger = False
    day_trigger = False

    while True:

        # set max_day
        if current_month == 3 or current_month == 5 or current_month == 8 or current_month == 10:
            max_day = 30
        elif current_month == 1: # february
            max_day = 28

            if current_year % 4 == 0: # leap year
                if current_year % 100 == 0:
                    # no leap year on centuries
                    pass
                    if current_year % 400 == 0:
                        # except when divisible by 400
                        max_day = 29
                    else:
                        pass
                else:
                    max_day = 29
        else: # rest of the months
            max_day = 31

        print(current_year, current_month, max_day)

        while True:
            if month_trigger and current_day > end_day:
                day_trigger = True # set end day trigger
                break

            if current_year > 1900 and current_day == 1 and day_name == specified_day: # January + Day of week
                number_of_specified += 1 # falls on the first of the month

            if current_day > max_day: # end case
                break
            current_day += 1
            day_name += 1
            if day_name > day_name_max: # cycles through day names
                day_name = 0

        # end case

        if year_trigger and month_trigger and day_trigger: # the correct month and year end time
            return number_of_specified

        # increment to next month
        current_month += 1

        if current_month >= max_month: # checks if next year; increment
            current_month = 0
            current_year += 1

        # set end year trigger
        if current_year == end_year:
            year_trigger = True

        if year_trigger and current_month == last_month: # set end month trigger
            month_trigger = True

        current_day = 1


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

print('')
print('numebr of usndays that fell on the first of each month from 1901 January 1 to 2000 December 31')
print(number_of_days('Sunday', 1, 'Monday', 'January', 1900, 31, 'December', 2000)))
print('')

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
