import datetime
import time
from bs4 import BeautifulSoup
import requests
from datetime import date  

# or state parks yurt finder

#user input to make search request?
td = date.today() # Use the today method and assign it to the td variable.  
year = td.strftime("%Y")
month = td.strftime("%m")
day = td.strftime("%d")
print("Today's date in Python is: ", day, month, year)
 
# scrape 1.0
html_text = requests.get('https://oregonstateparks.reserveamerica.com/unifSearchResults.do').text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

yurts = soup.find('div', class_ = 'facility_view_card redesigned')
print(yurts)
