import math

import pandas as pd
import sklearn

BTCUSDT_data = pd.read_csv('Binance_BTCUSDT_d.csv')
print(BTCUSDT_data.head())
"""columns:['unix' 'date' 'symbol' 'open' 'high' 'low' 'close' 'Volume BTC'
 'Volume USDT' 'tradecount']"""
BTCUSDT_data.reset_index()
BTCUSDT_data['daily_return'] = ((BTCUSDT_data.close - BTCUSDT_data.open) * 100) / BTCUSDT_data.open
all_points = []

def min_max_normalize(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []
  for i in lst:
    normalized.append((i - minimum) / (maximum - minimum))
  return normalized

BTCUSDT_data['Volume USDT'] = min_max_normalize(BTCUSDT_data['Volume USDT'])
BTCUSDT_data['Volume BTC'] = min_max_normalize(BTCUSDT_data['Volume BTC'])
BTCUSDT_data['tradecount'] = min_max_normalize(BTCUSDT_data['tradecount'])
BTCUSDT_data['daily_return_normalized'] = min_max_normalize(BTCUSDT_data['daily_return'])

def distance(a,b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i]) ** 2
    return sum ** 0.5

