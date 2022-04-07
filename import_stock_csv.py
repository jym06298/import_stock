import requests
import json
import pandas as pd
import csv
import datetime
import time


def checkRequest(data):
  if data['empty']:
    print("api request came back empty")
  else:
    print("Success")

def get_stock_data_to_csv(ticker_list):


    for ticker in ticker_list:
        price_url = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(ticker)
        api_key = "EXDEQZTLBS2PNWXDDJ9AOJHPX15WSSRI"

        payload = {'apikey':api_key,
           'periodType':'year',
           'frequencyType':'daily',
           'frequency':'1',
           'period':'10',
           'needExtendedHoursData':'true'
           
           }

        request = requests.get(url = price_url, params = payload)
        data = request.json()

        checkRequest(data)
        
        df = pd.json_normalize(data['candles'])
        df['datetime'] = convert_epoch_datetime(df['datetime'])
        file_name = ticker + '.csv'
        df.to_csv(file_name)
        
def convert_epoch_datetime(dates):
  ser = []
  for i in dates:
    ser.append(datetime.datetime.fromtimestamp(i/1000.0).strftime('%Y%m%d'))
  return ser
    
milliseconds = int(time.time() * 1000)

ticker_str = input("Please enter ticker symbols seperated by a space: ")
ticker_list = []

for ticker in ticker_str.split(' '):
  ticker_list.append(ticker)

#ticker_list = ['TSLA', 'AAPL', 'MSFT', 'FB', 'NVDA']

get_stock_data_to_csv(ticker_list)






