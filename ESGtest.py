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
    print("ESG Grade Description:")
    print("CCC -> B -> BB -> BBB -> A -> AA -> AAA")
    print("\nAA -> AAA: A company leading its industry in managing the most significant ESG risks and opportunities")
    print("BB -> A: A company with mixed or unexceptional track record of ESG risks and opportunities relative to industry peers")
    print("CCC -> B: A company lagging its industry based on its high exposure and failure to manage significant ESG risks\n")
    print("Company Name: " + output[0]['company_name'])
    print("\nESG grades on a scale of AAA-CCC:")
    print("Environment Grade: " + output[0]['environment_grade'])
    print("Social Grade: " + output[0]['social_grade'])
    print("Governance Grade: " + output[0]['governance_grade'])

    print("\nESG Score on a scale from 0 - 1000: ")
    print("Environment Score: " + str(output[0]['environment_score']))
    print("Social Score: " + str(output[0]['social_score']))
    print("Governance Score: " + str(output[0]['governance_score']))
    print("Total ESG Score: " + str(output[0]['total']))

    return output[0]['company_name']

get_esg_data("jpm")