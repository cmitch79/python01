# nano faucet scraper 1.2
# cm 12/27/19

# mods
# 12/27/19 - changed the indents on the write to csv try.

# python -m pip install nameofpackage

# scrape nano faucet balance every 60 min
# determine if it's worth notifying with an email
# if it is, send an email notifying high balance and write the value to a csv doc
# v 1.1 look into adding try/except for scraper
# FINALLY BLOCK NEEDED?
# ERROR HANDLING ... DO YOU HANDLE ERRORS @ EACH STEP OF THE WAY? ...
# ...(TRY TO GET URL, TRY TO GET VALUE, TRY TO WRITE TO CSV, TRY TO EMAIL)? OR, IS THERE A WAY TO HANDLE GLOBALLY?

from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
from decimal import Decimal
import csv
from datetime import datetime

#url = requests.get('https://getnanoD.co.uk/')

try:
    url = requests.get('https://getnano.co.uk/')
    soup = BeautifulSoup(url.content, 'html.parser')
    input = soup.find(attrs={"id": "faucetBalance"})
    output = Decimal(input['value'])

except:
    print('Invalid site or value')

# Add the value to a csv file
else:
    try:
        with open('scrape.csv', 'a', newline='') as csvfile:
            columnHeader = ['balance', 'datetime']
            writer = csv.DictWriter(csvfile, fieldnames=columnHeader)
            writer.writerows(
                [{'balance': output, 'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}])
        print(str(output) + " balance written to scrape.csv")
    except:
        print("Couldn't print to scrape.csv")

# value is a string and needs to be converted
if output <= .5:
    pass
else:
    msg = EmailMessage()
    msg.set_content('Balance is: ' + '<font size="20" color="blue">' +
                    str(output) + '</font>', subtype='html')
    msg['Subject'] = 'Nano Faucet'
    msg['From'] = "testpycm@gmail.com"
    msg['To'] = "testpycm@gmail.com"

# Send the message via our own SMTP server

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("testpycm@gmail.com", "0m9XgH#6p#")
    server.send_message(msg)
    server.quit()
    print('email sent')
