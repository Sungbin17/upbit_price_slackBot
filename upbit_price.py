import urllib.request, json
from env import Upbit_ETH_daily_url
from urllib.request import Request, urlopen

response = Request(Upbit_ETH_daily_url, headers={'User-Agent': 'Mozilla/5.0'})

data = json.loads(urlopen(response).read())

yesterday_ETH_price = data[1]

date = yesterday_ETH_price.get('candleDateTime')[:10]

highPrice = yesterday_ETH_price.get('highPrice')

lowPrice = yesterday_ETH_price.get('lowPrice')

averagePrice = (highPrice + lowPrice) / 2

won = 10000000 / averagePrice

won = round(won, 3)

print(date, highPrice, lowPrice, averagePrice)

while True:
	print(str(date) + ' 1ETH = ' + str(averagePrice) + ' 1천만원당 ' + str(won) + 'ETH' + ' 기준 - 저:' + str(lowPrice) + ' 고: ' + str(highPrice) , '(업비트)' )
	time.sleep(1000)