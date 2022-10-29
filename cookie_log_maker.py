'''
COOKIE FORMAT

16 random alpha numeric characters
comma
YYYY-MM-DD
T
Random hour
colon
Random minute
colon
00+00:00
'''

import csv
import string
import random

# returns a length 16 string made of uppercase letters, lowercase letters, and numbers


def random_alphanumeric():
    randomness = list(string.ascii_lowercase +
                      string.ascii_uppercase + string.digits)
    random_string = ''

    for i in range(16):
        random_string += random.choice(randomness)
    return random_string

# returns a random date in YYYY-MM-DD format


def random_date_generator():
    # decided to make year 2022
    year = 2022
    month_day = [[1, 31], [2, 28], [3, 31], [4, 30], [5, 31],
                 [6, 30], [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]

    random_month = random.choice(month_day)[0]
    random_day = random.randint(1, random.choice(month_day)[1])

    if random_month < 10:
        return_month = "0" + str(random_month)
    else:
        return_month = str(random_month)

    if random_day < 10:
        return_day = "0" + str(random_day)
    else:
        return_day = str(random_day)

    return str(year) + "-" + return_month + "-" + return_day

# returns random hour in HH format


def random_hour_generator():
    random_hour = random.randint(0, 23)
    if random_hour < 10:
        return_hour = "0" + str(random_hour)
    else:
        return_hour = str(random_hour)

    return return_hour

# returns random minute in MM format


def random_minute_generator():
    random_minute = random.randint(0, 59)
    if random_minute < 10:
        return_minute = "0" + str(random_minute)
    else:
        return_minute = str(random_minute)

    return return_minute

# makes/writes into csv. writes num_of_tests tests


def cookie_log_maker(csv_name, num_of_tests):
    with open(csv_name + ".csv", "w", newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(["cookie", "timestamp"])

        # makes ten cookie IDs
        cookie_list = []
        for i in range(10):
            cookie_list.append(random_alphanumeric())

        # writes tests in csv
        for i in range(num_of_tests):
            thewriter.writerow([random.choice(cookie_list), random_date_generator()
                                + "T" + random_hour_generator() + ":"
                                + random_minute_generator() + ":" + "00+00:00"])


# make it!
cookie_log_maker("mega_tester", 1000)
