# Python script to send api request to next-birthday endpoint and capture the response.
import main
import requests
import json
import jsonschema
import datetime

def getBD(my_unit, my_date):
    # send api request to endpoint
    p = {"dateofbirth": '', "unit": ''}
    p["dateofbirth"] = my_date
    p["unit"] = my_unit
    resp = requests.get("https://p9fwi1d77e.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday",params=p)
    json_response = resp.json()
    code = resp.status_code
    message = (json_response["message"])
    return (code,message)