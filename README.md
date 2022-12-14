# Quantcast Summer Internship Program Coding Exercise

The program in this coding exercise returns the Cookie ID that appears the most often given a date "-d".

This coding exercise is written in Python. \
Running the program: input below command into terminal.
````md
python .\most_active_cookie.py .\cookie_log.csv -d DATE
````
Where DATE is in YYYY-MM-DD format (such as 2018-12-09). Do not include quotations around the date.

You can also run this code with no date argument as such:
````md
python .\most_active_cookie.py .\cookie_log.csv
````
This returns the most often appeared Cookie ID regardless of date.

I also wrote cookie_log_maker.py to make a random cookie log for testing purposes.

I wrote the code such that a user that makes any syntax mistakes will understand what mistake they have made. 

### My Files

- most_active_cookie.py: My main program. Finds the most active cookie.
- cookie_log.csv: The given csv file from the problem statement.
- mega_tester.csv: A csv file made by cookie_log_maker.py. Currently has 1000 Cookie IDs, but this can be changed.
- cookie_log_maker.py: A program that makes a new CSV file or edits an existing CSV file. It writes in custom Cookie IDs.
- test.ipynb: A notebook I used to play around with the code.