import pandas as pd

BTCUSDT_data = pd.read_csv('Binance_BTCUSDT_d.csv')
#print(BTCUSDT_data.columns.values)
"""columns:['unix' 'date' 'symbol' 'open' 'high' 'low' 'close' 'Volume BTC'
 'Volume USDT' 'tradecount']"""
BTCUSDT_data.reset_index()
#Calculating the daily return
BTCUSDT_data['daily_return'] = ((BTCUSDT_data.close - BTCUSDT_data.open) * 100) / BTCUSDT_data.open
#print(BTCUSDT_data.head())
clusters_based_on_daily_returns = [[],[],[]]
for i in range(len(BTCUSDT_data)):
    if -0.1 < BTCUSDT_data['daily_return'][i] and BTCUSDT_data['daily_return'][i] < 0.1:
        clusters_based_on_daily_returns[1].append(BTCUSDT_data['date'][i])
    elif BTCUSDT_data['daily_return'][i] >= 0.1:
        clusters_based_on_daily_returns[2].append(BTCUSDT_data['date'][i])
    else:
        clusters_based_on_daily_returns[0].append(BTCUSDT_data['date'][i])

print(clusters_based_on_daily_returns[0])
print(clusters_based_on_daily_returns[1])
print(clusters_based_on_daily_returns[2])

