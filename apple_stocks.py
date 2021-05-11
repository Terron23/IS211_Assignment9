import requests
from bs4 import BeautifulSoup
import json
import ssl

# url = 'http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices'
print("test")
url = 'https://www.nasdaq.com/market-activity/stocks/aapl/historicals'
context = ssl._create_unverified_context()
page = requests.get(url)
print(page)
soup = BeautifulSoup(page.read())

def yahoo_apple_stock():
    data = []
    fhandler = soup.find_all('tr')
    
    for rows in fhandler:
       
            if len(rows.find_all(('td', {'class': 'historical-data__row'}))) == 7:
                date = rows.contents[0].get_text()
                close = rows.contents[5].get_text()
                data.append((date, close))
                json_string = {
                "Date": date,
                "Closed Stock Price": close,
                }
                print(json.dumps(json_string))
    
    return data
    


yahoo_apple_stock()