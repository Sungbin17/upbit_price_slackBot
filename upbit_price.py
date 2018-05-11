import urllib.request, json
from env import Upbit_ETH_daily_url

response = urllib.request.urlopen(Upbit_ETH_daily_url)

data = json.loads(response.read())

print(data[0])