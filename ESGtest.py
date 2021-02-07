import requests
import json

def get_esg_data(company):
    url = "https://esg-environmental-social-governance-data.p.rapidapi.com/search"

    querystring = {"q":company}

    headers = {
        'x-rapidapi-key': "9b4298684cmshec60042afe23ed8p1d47d4jsne6f311bf479a",
        'x-rapidapi-host': "esg-environmental-social-governance-data.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)

    #print(type(response.text))

    #json.loads(response)

    #Convert to json object
    output = json.loads(response.text)
    #print(output)

    print(output)

    #print(type(output))
    #Access specific attributes
    print("OUTPUT: " + output[0]['company_name'])
    print(output[0]['total'])

    return output[0]['company_name']

get_esg_data("aapl")