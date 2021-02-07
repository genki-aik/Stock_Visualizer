import requests
import datetime
import time
import json
import pandas as pd
import matplotlib.pyplot as plt

def stock_info(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

    querystring = {"symbol":ticker,"region":"US"}

    headers = {
        'x-rapidapi-key': "9b4298684cmshec60042afe23ed8p1d47d4jsne6f311bf479a",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = json.loads(response.text)
    #print(type(result))
    #print(result.keys())
    print("Latest Data for " + ticker + ":")
    print("Date: " + datetime.datetime.fromtimestamp(int(result['prices'][0]['date'])).strftime('%Y-%m-%d %H:%M:%S'))
    print("Open Price: % 5.2f" %(result['prices'][0]['open']))
    print("High: % 5.2f" %(result['prices'][0]['high']))
    print("Low: % 5.2f" %(result['prices'][0]['low']))
    print("Close Price: % 5.2f" %(result['prices'][0]['close']))
    
    return result['prices'][0]['open']

#print(response.text)
#print(
#    datetime.datetime.fromtimestamp(
#        int("1612535400")
 #   ).strftime('%Y-%m-%d %H:%M:%S')
#)

# s = "02/05/2021"
# print(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
dt_string = "02/05/2021 09:30:00"
dt_object = datetime.datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
#print(time.mktime(dt_object.timetuple()))

def date_convert(month, date, year):
    date_string = month + "/" + date + "/" + year + " 09:30:00"
    date_object = datetime.datetime.strptime(date_string, "%m/%d/%Y %H:%M:%S")
    return time.mktime(date_object.timetuple())

stock_info('GME')
