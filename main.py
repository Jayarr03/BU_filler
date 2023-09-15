import requests
import json
import pandas as pd
import config

baseURL = "https://james-rabe.iriusrisk.com//api/v1/"

bu_refID = "BU_refID" #its actually using the name of the business unit and not the business unit ID

business_unit_endpoint = f"{baseURL}businessunits/{bu_refID}/users"

def bu_user_fill(bu_refID,username):

    business_unit_endpoint = f"{baseURL}businessunits/{bu_refID}/users"

    payload = json.dumps({
      "usernames": [
        f"{username}"
      ]
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api-token': config.API_key
    }

    response = requests.request("PUT", business_unit_endpoint, headers=headers, data=payload)

    if response.status_code == 201:
        print(f"Status code 201: {username} was added successfully!")
    else:
        print(f"Status code {response.status_code}: {username} was not added!")


data = pd.read_csv(r'C:\Users\jrabe_iriusrisk\PycharmProjects\pythonProject2\bu_filler.csv')  # Replace 'your_spreadsheet.csv' with the actual file name and path

counter = 1

for index, row in data.iterrows():

  counter += 1

  #create a spreadsheet with column headers and match those the variables in this script.

  bu_refID = str(row['bu_refID'])
  username = str(row['username'])

  bu_user_fill(bu_refID,username)