import urllib.request, json
from env import Upbit_ETH_daily_url, SLACK_BOT_TOKEN, bot_test_channel
from urllib.request import Request, urlopen
import time
import datetime
import schedule
from slackclient import SlackClient


def send_price_message():
	slack_token = SLACK_BOT_TOKEN
	response = Request(Upbit_ETH_daily_url, headers={'User-Agent': 'Mozilla/5.0'})
	data = json.loads(urlopen(response).read())
	sc = SlackClient(slack_token)
	yesterday_ETH_price = data[1]
	date = yesterday_ETH_price.get('candleDateTime')[:10]
	highPrice = yesterday_ETH_price.get('highPrice')
	lowPrice = yesterday_ETH_price.get('lowPrice')
	averagePrice = (highPrice + lowPrice) / 2
	won = 10000000 / averagePrice
	won = round(won, 3)
	show_price = str(date) + ' 1ETH = ' + str(averagePrice) + ' 1천만원당 ' + str(won) + 'ETH' + ' 기준 - 저:' + str(lowPrice) + ' 고: ' + str(highPrice) + ' (업비트)' 
	print(show_price)
	sc.api_call("chat.postMessage", channel=bot_test_channel, text=show_price)

	
schedule.every().day.at("10:00").do(send_price_message)

while True:
	schedule.run_pending()
	time.sleep(1)
