# This is a Python test script to execute to validate next-birthday endpoint works correctly.
# dob - date of user's birth in YYYY-MM-DD format
# unit - in which units you want to see the result (available options: hour/day/week/month)

import gettimforBD
import main
import datetime

# data required for the test
t = datetime.date.today()
yestr = str(t - datetime.timedelta(days = 1))
tomo = str(t + datetime.timedelta(days = 1))
tody_date = str(t)
next_month = str(t + datetime.timedelta(days = 30))
within_month = str(t + datetime.timedelta(days = 29))
last_month = str(t - datetime.timedelta(days = 30))
next_week = str(t + datetime.timedelta(days = 7))
last_week = str(t - datetime.timedelta(days = 7))
within_week = str(t + datetime.timedelta(days = 5))
within_lastweek = str(t - datetime.timedelta(days = 5))
greater_than_year = str(t + datetime.timedelta(days = 367))
p = {"unit1":'hour',"unit2":'day',"unit3":'week',"unit4":'month',
     "dob1":'2020-02-28',"dob2": tody_date,"dob3":yestr,"dob4": tomo,
     "dob5": '2020-02-29',"dob6":'2019-06-31',"dob7":next_month,
     "dob8":within_month,"dob9":last_month,"dob10":next_week,
     "dob11":last_week,"dob12":within_week,"dob13":within_lastweek,
     "dob14": greater_than_year}

# Test case Function

def test_get_hours_left_for_BirthDay_dob_is_Feb28():
    dob = p["dob1"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200,myresult)

def test_get_hours_left_for_BirthDay_dob_is_today():
    dob = p["dob2"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200,myresult)

def test_get_days_left_for_BirthDay_dob_is_today():
    dob = p["dob2"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200,myresult)

def test_get_weeks_left_for_BirthDay_dob_is_today():
    dob = p["dob2"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200,myresult)

def test_get_months_left_for_BirthDay_dob_is_today():
    dob = p["dob2"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200,myresult)

def test_get_hours_left_for_BirthDay_dob_is_tomorrow():
    dob = p["dob4"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit,dob)
    assert gettimforBD.getBD(unit,dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_is_tomorrow():
    dob = p["dob4"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit,dob)
    assert gettimforBD.getBD(unit,dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_is_tomorrow():
    dob = p["dob4"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit,dob)
    assert gettimforBD.getBD(unit,dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_is_tomorrow():
    dob = p["dob4"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit,dob)
    assert gettimforBD.getBD(unit,dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_is_yesterday():
    dob = p["dob3"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_is_yesterday():
    dob = p["dob3"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_is_yesterday():
    dob = p["dob3"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_is_yesterday():
    dob = p["dob3"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_is_in_a_month():
    dob = p["dob7"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_is_in_a_month():
    dob = p["dob7"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_is_in_a_month():
    dob = p["dob7"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_is_in_a_month():
    dob = p["dob7"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_is_within_a_month():
    dob = p["dob8"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_is_within_a_month():
    dob = p["dob8"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_is_within_a_month():
    dob = p["dob8"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_is_within_a_month():
    dob = p["dob8"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_is_in_last_month():
    dob = p["dob9"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_is_in_last_month():
    dob = p["dob9"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_is_in_last_month():
    dob = p["dob9"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_is_in_last_month():
    dob = p["dob9"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_is_in_next_week():
    dob = p["dob10"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_is_in_next_week():
    dob = p["dob10"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_is_in_next_week():
    dob = p["dob10"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_is_in_next_week():
    dob = p["dob10"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_is_in_last_week():
    dob = p["dob11"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_is_in_last_week():
    dob = p["dob11"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_is_in_last_week():
    dob = p["dob11"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_is_in_last_week():
    dob = p["dob11"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_is_within_week():
    dob = p["dob12"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_is_within_week():
    dob = p["dob12"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_is_within_week():
    dob = p["dob12"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_is_within_week():
    dob = p["dob12"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_is_within_week():
    dob = p["dob12"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_is_within_last_week():
    dob = p["dob13"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_is_within_last_week():
    dob = p["dob13"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_is_within_last_week():
    dob = p["dob13"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_is_within_last_week():
    dob = p["dob13"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_hours_left_for_Birthday_dob_is_on_Feb29():
    dob = p["dob5"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit,dob)
    assert gettimforBD.getBD(unit,dob) == (200, myresult)

def test_get_hours_left_for_Birthday_dob_is_on_March1():
    dob = '2022-03-01'
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit,dob)
    assert gettimforBD.getBD(unit,dob) == (200, myresult)

def test_get_hours_left_for_BirthDay_dob_falls_more_than_year_from_current_date():
    dob = p["dob14"]
    unit = p["unit1"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_days_left_for_BirthDay_dob_falls_more_than_year_from_current_date():
    dob = p["dob14"]
    unit = p["unit2"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_weeks_left_for_BirthDay_dob_falls_more_than_year_from_current_date():
    dob = p["dob14"]
    unit = p["unit3"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_get_months_left_for_BirthDay_dob_falls_more_than_year_from_current_date():
    dob = p["dob14"]
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)


def test_get_days_left_for_Birthday_dob_is_Feb29_NonLeapYear_2021():
    dob = '2021-02-29'
    unit = 'day'
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200,myresult)

def test_get_days_left_for_Birthday_dob_is_Feb29_LeapYear_2016():
    dob = '2016-02-29'
    unit = 'day'
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200,myresult)

def test_invalid_unit_format():
    dob = '2020-05-03'
    unit = 'days'
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_Invalid_date_format():
    dob = '2020/05/03'
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test1_to_validate_year_in_range_0001_to_9999():
    dob = '0001-01-01'
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test2_to_validate_year_in_range_0001_to_9999():
    dob = '9999-01-01'
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_to_validate_year_0000():
    dob = '0000-01-01'
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)

def test_to_validate_year_10000():
    dob = '0000-01-01'
    unit = p["unit4"]
    myresult = main.daysforbirthday(unit, dob)
    assert gettimforBD.getBD(unit, dob) == (200, myresult)