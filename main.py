# This is a Python script that calculates the amount of time left before user's next birthday.
# mydate - date of user's birth in YYYY-MM-DD format
# unit - in which units you want to see the result (available options: hour/day/week/month)

import datetime
import re

def daysforbirthday(unit, mydate):
    # Check if the date or unit is null
    if (mydate == '' or unit == ''):
        return ("Please specify both query parameter dateofbirth and unit")

    # Assign ErrorMessage
    ErrorMessage = "Please specify dateofbirth in ISO format YYYY-MM-DD"

    # verify that date format is as expected in the Request parameters
    if not (re.search("^\d{4}-\d{2}-\d{2}$", mydate)):
        return ErrorMessage

    # validate that the date is valid
    year, month, date = mydate.split('-')
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(date))
    except ValueError:
        isValidDate = False

    if (isValidDate):
        pass
    else:
        return ErrorMessage

    # Validate date pattern as per dat of birth request parameter
    if not (re.search("^\d{4}$", year)):
        return ErrorMessage
    elif not (re.search("^(1[0-2]|0[1-9])$", month)):
        return ErrorMessage
    elif not (re.search("^(3[01]|[12][0-9]|0[1-9])$", date)):
        return ErrorMessage
    elif int(year) == 0:
        return ErrorMessage

    # convert date parameter to int type
    year = int(year)
    month = int(month)
    date = int(date)

    # Calculate today's and given birth date
    birth = datetime.date(year, month, date)
    today = datetime.date.today()

    # Condition for calculating no of day, hours, weeks, months to next birthday
    if (today.day == birth.day
        and birth.month >= today.month
        and birth.year <= today.year
    ):
        nextBirthdayYear = today.year
    elif (birth.year > today.year):
        nextBirthdayYear = birth.year
    elif (
            today.month == birth.month
            and today.day >= birth.day
            or today.month > birth.month
    ):
        nextBirthdayYear = today.year + 1

    else:
        nextBirthdayYear = today.year

    # calculating next birthday for leaplings, leapers
    if (birth.month == 2 and birth.day == 29):
        if (nextBirthdayYear % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    newday = birth.day
                    newmonth = birth.month
                else:
                    newday = 1
                    newmonth = birth.month + 1
            else:
                newday = birth.day
                newmonth = birth.month
        else:
            newday = 1
            newmonth = birth.month + 1

    else:
        newday = birth.day
        newmonth = birth.month

    # Arrive at nextBirthday
    nextBirthday = datetime.date(nextBirthdayYear, newmonth, newday)

    # Calculate Next birthday
    diff = nextBirthday - today
    diff_hours = diff.days * 24
    diff_months = diff.days // 30
    diff_week = diff.days // 7

    # return result based on mentioned unit parameter
    if unit == 'hour':
        s = ("{} hours left".format(diff_hours))
        return s
    elif unit == 'day':
        s = ("{} days left".format(diff.days))
        return s
    elif unit == 'week':
        s = ("{} weeks left".format(diff_week))
        return s
    elif unit == 'month':
        s = ("{} months left".format(diff_months))
        return s
    else:
        return ("Please specify the correct unit")



if __name__ == '__main__':
    daysforbirthday('day','2021-03-29')


