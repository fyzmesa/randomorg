import requests
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import random

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Replace YOUR_API_KEY with your actual API key
api_key = 'APIKEY'

url = 'https://api.random.org/json-rpc/2/invoke'
headers = {'content-type': 'application/json'}
payload = {
    'jsonrpc': '2.0',
    # 'method': 'generateIntegers',
    # 'params': {
    #     'apiKey': api_key,
    #     'n': 1,
    #     'min': 0,
    #     'max': 1000000000,
    #     'replacement': True
    #    
    'method': 'generateDecimalFractions',
        'params': {
            'apiKey': api_key,
            'n': 1,
            'decimalPlaces': 10
            },
        
    'id': 1
}

response = requests.post(url, verify=False, data=json.dumps(payload), headers=headers).json()
random_numbers = response['result']['random']['data']
# print(random_numbers[0])

random_float = random.uniform(0.0, 1.0)
rounded_float = round(random_float, 10)
# print(rounded_float)
rounded_float=1

finalNumber = random_numbers[0]*rounded_float
print(finalNumber)

if finalNumber < 0.166667:
    print("1")
elif 0.166667 < finalNumber < 0.333333:
    print("2")
elif 0.333333 < finalNumber < 0.5:
    print("3")
elif 0.5 < finalNumber < 0.666667:
    print("4")
elif 0.666667 < finalNumber < 0.833334:
    print("5")
else:
    print("6")
