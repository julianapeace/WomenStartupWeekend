import requests
import json


state = 'state:02'
year = '2012'
key = 'e36c64ad9bd505760e317fb61b63c03717bc68ff'

payload = {'get':'Emp' , 'for': state, 'year':year, 'key' : key}

response = requests.get("https://api.census.gov/data/timeseries/qwi/se", params=payload)


#   headers={
#     "X-Mashape-Key": "DHIgOSjvISmshwNj2QfspbJAfROxp1KQPe0jsnuoKKCaVA7y6J",
#     "X-Mashape-Host": "faceplusplus-faceplusplus.p.mashape.com"
#   }
# )
r = response.json()
# r = json.loads(response)
print(r)
# print(type(response))
