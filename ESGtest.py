import requests
import json
import matplotlib.pyplot as plt

def get_esg_data(company):
    url = "https://esg-environmental-social-governance-data.p.rapidapi.com/search"

    querystring = {"q":company}

    headers = {
        'x-rapidapi-key': "9b4298684cmshec60042afe23ed8p1d47d4jsne6f311bf479a",
        'x-rapidapi-host': "esg-environmental-social-governance-data.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #Convert to json object
    output = json.loads(response.text)
    print(output)

    e_score = output[0]['environment_score']
    s_score = output[0]['social_score']
    g_score = output[0]['governance_score']
    total_score = output[0]['total']

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
    print("Environment Score: " + str(e_score))
    print("Social Score: " + str(s_score))
    print("Governance Score: " + str(g_score))
    print("Total ESG Score: " + str(total_score))

    # Pie Chart
    max = e_score
    labels = 'Environment', 'Social', 'Governance'

    if max < s_score:
        max = s_score
    
    if max < g_score:
        max = g_score
    sizes = [e_score, s_score, g_score]
    
    # Make sure the largest slice will "explode"
    if max == e_score:
        explode = (0.1, 0, 0)
    elif max == s_score:
        explode = (0, 0.1, 0)
    else:
        explode = (0, 0, 0.1)
    
    #explode = (0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, textprops = dict(color="black"))
    ax1.axis('equal')
    ax1.set_title(output[0]['company_name'] + "ESG Pie Chart")

    plt.show()
    plt.close()
    return output[0]['company_name']

#get_esg_data("jpm")