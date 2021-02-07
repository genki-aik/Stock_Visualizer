import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt


url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

querystring = {"symbol":"GME","region":"US"}

headers = {
    'x-rapidapi-key': "9b4298684cmshec60042afe23ed8p1d47d4jsne6f311bf479a",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
print(
    datetime.datetime.fromtimestamp(
        int("1612449000")
    ).strftime('%Y-%m-%d %H:%M:%S')
)