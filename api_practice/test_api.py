#c. mitchell 1/2/2019
# this is a program will hit an api, return the data and chart it
# for Sheets api client library, install using:  python -m pip install --upgrade google-api-python-client
# sheet url:  https://docs.google.com/spreadsheets/d/1KueQQhc-dCTN0sgSQbN64QtVEAOlpkENcmo6dRPcAkU/edit#gid=0

import requests

response = requests.get('http://www.nike.com/')
print(response.status_code)
