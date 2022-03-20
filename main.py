# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import timedelta
from random import randrange
from datetime import datetime


def random_date(start, end):
    delta = end - start
    int_delta = delta.days
    random_day = randrange(int_delta)
    return (start + timedelta(days=random_day)).date()


def get_date_day(d):
    if 2 == d.weekday():
        return "אין לי ויניגרט"
    return d


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    minDate = input("please enter the minimum date: ")
    maxDate = input("please enter the maximum date: ")
    d1 = datetime.strptime(minDate, '%Y-%m-%d')
    d2 = datetime.strptime(maxDate, '%Y-%m-%d')
    print(get_date_day(random_date(d1, d2)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
