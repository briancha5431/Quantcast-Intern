# for command line arguments (required)
import sys

# reading the csv file
import csv

'''
helper function: "date_checker"
input: a date that is a string
output: returns true if the string is in the proper format "YYYY-MM-DD" and if the date
is valid.
'''


def date_checker(date):
    # dictionary "month_day"
    # key: months numbered in order
    # value: number of days in that month (ex: January has 31 days)
    month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # Must have proper "YYYY-MM-DD" format. If it does not, it will return False.
    # Checks if length of string is 10 and if dashes are in the right place.
    if len(date) != 10 and date[4] != "-" and date[7] != "-":
        return False

    # Months and Days must be in calendar. For example, there is no 13th month and
    # the month of February does not have 31 days.
    else:
        try:
            year = int(date[0:4])
            month = int(date[5:7])
            day = int(date[8:10])
        except:
            return False

        if month > 12:
            return False
        elif month == 2 and year % 4 == 0:      # checks for leap years
            if day > 29:
                return False
        elif day > month_day[month]:
            return False
    return True


'''
helper function: "active_finder"
input: a csv_file as a string and a date in YYYY-MM-DD format as a string
    Note: the date can also be "". This means no date was inputted and we
    return the most active cookie for the entire CSV file
output: doesn't return anything, but prints out most active cookies
'''


def active_finder(csv_file, date):

    # counts the max number of times any cookie was in log
    max_counter = 0
    # in case no date was inputted
    if date == "":

        # dictionary "non_date"
        # key: the cookie
        # value: the number of times the cookie was seen in log
        non_date = {}

        # opens csv
        with open(csv_file, 'r') as checker:
            csv_reader = csv.reader(checker)

            for line in csv_reader:
                # we don't include the "cookie", "timestep" line
                if line[0] != "cookie":
                    # if new cookie ID is encountered, put into non_date dictionary
                    if line[0] not in non_date:
                        # just makes sure to increment max_counter
                        if max_counter < 1:
                            max_counter += 1
                        non_date[line[0]] = 1
                    # else, increment count (the value) of cookie ID by one
                    else:
                        non_date[line[0]] += 1
                        # if the number of encounters is greater than max_counter,
                        # make max_counter equal to that cookie's number of encounters.
                        if non_date[line[0]] > max_counter:
                            max_counter = non_date[line[0]]

        # prints the cookies which appeared the most in the log
        for x in non_date:
            if non_date[x] == max_counter:
                print(x)

    # when a date was inputted
    else:
        # dictionary "with_date"
        # key: the cookie
        # value: the number of times the cookie was seen in log
        with_date = {}

        # opens csv
        with open(csv_file, 'r') as checker:
            csv_reader = csv.reader(checker)

            for line in csv_reader:
                # we don't include the "cookie", "timestep" line
                if line[0] != "cookie":
                    # if new cookie ID is encountered, put into with_date dictionary
                    # AND the date from the CSV file must be equal to the inputted date
                    if line[0] not in with_date and line[1][0:10] == date:
                        # just makes sure to increment max_counter
                        if max_counter < 1:
                            max_counter += 1
                        with_date[line[0]] = 1
                    # else, increment count (the value) of cookie ID by one
                    elif line[1][0:10] == date:
                        with_date[line[0]] += 1
                        # if the number of encounters is greater than max_counter,
                        # make max_counter equal to that cookie's number of encounters.
                        if with_date[line[0]] > max_counter:
                            max_counter = with_date[line[0]]

        # prints the cookies which appeared the most in the log
        for x in with_date:
            if with_date[x] == max_counter:
                print(x)

    # oh no! no matches
    if max_counter == 0:
        print("Sorry, there was no cookies that matched your criteria.")


'''
Start here! :)
Python Specific: args[0] WILL ALWAYS BE most_active_cookie.py.
Basically, just by running this program through the terminal, we will always have at 
least one argument.
'''


def main(argv):

    # There is only one argument. Attempts to run this program without at least two arguments
    # will result in an error.
    if len(sys.argv) == 1:
        raise ValueError("Please input CSV file as a command line argument")

    # There is at least two arguments, but the second argument is not a CSV file. This
    # results in an error.
    elif len(sys.argv) >= 2 and sys.argv[1][-3:] != "csv":
        raise ValueError(
            "Incorrect File Format. Please input CSV file (should end in csv)")

    # There is EXACTLY two arguments and the second argument is a CSV file. This should
    # return the most active cookie for the ENTIRE CSV FILE
    elif len(sys.argv) == 2 and sys.argv[1][-3:] == "csv":
        active_finder(sys.argv[1], "")

    # There is at least three arguments and the second argument is a CSV file.
    elif len(sys.argv) >= 3 and sys.argv[1][-3:] == "csv":

        # The third argument is not "-d", which results in an error
        if sys.argv[2] != "-d":
            raise ValueError(
                '''Incorrect parameter input. Available parameters are "-d".''')

        # If the third argument is "-d", there MUST be a fourth argument (the date).
        # If there is no fourth argument, then an error is raised
        elif len(sys.argv) != 4:
            raise ValueError(
                '''No date inputted after raising "-d" parameter. The date format is "YYYY-MM-DD"''')

        # If there is a fourth argument, but it is not in the proper date format, it will
        # raise an error
        elif date_checker(sys.argv[3]):
            active_finder(sys.argv[1], sys.argv[3])

        else:
            raise ValueError("You inputted an impossible date.")


# pass through argv into python function
if __name__ == '__main__':
    main(sys.argv)
