import requests
import json
import time
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from ReadWriteToFile import readDataFromFile, writeDataToFile
import settings

def getLatestPrices():
    previous_price = float(readDataFromFile())
    print("previous: "+str(previous_price))
    current_price = getMELDPrice()
    print("new: " + str(current_price))
    writeDataToFile(current_price)

    calculatePCTChange(previous_price,current_price )

def getMELDPrice():
  url = 'https://api-mainnet-prod.minswap.org/coinmarketcap/v2/pairs'
  headers = {
    'Accepts': 'application/json',
    'Accept-Encoding' : 'deflate, gzip',
  }
  session = requests.Session()
  session.headers.update(headers)

  try:
    response = session.get(url)
    data = json.loads(response.text)
    current_price= round(float(data['6ac8ef33b510ec004fe11585f7c5a9f0c07f0c23428ab4f29c1d7d104d454c44_lovelace']['last_price']),4)
    print(current_price)
    return(current_price)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

def calculatePCTChange(previous_price, current_price):
    pct_change = round((current_price - previous_price) * 100 / previous_price,2)
    print("% Change = " + str(pct_change))
    if abs(pct_change) > 5:
        notifyTG(pct_change)

def notifyTG(pct_change):

    TOKEN = settings.SECRETTOKEN
    chat_id = "1012804577"
    message = "Price change in 5 minutes: " + str(pct_change) + " %"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={settings.CHATID}&text={message}"
    print(requests.get(url).json())
getLatestPrices()
