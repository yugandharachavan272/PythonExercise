import requests
import logging
import sys
import json

api_key = "rbzVYGZTS_iR1fNo_Fvx"
share_name = "BOM531219"
logging.basicConfig(format='%(levelname)-10s: %(message)s', filename='webAPI.log', filemode='w', level=logging.DEBUG)
url = "https://www.quandl.com/api/v3/datasets/BSE/{}.json?api_key={}".format(share_name, api_key)

response = requests.get(url)
if response.status_code != 200:
    logging.error('ERROR: response type {}'.format(response))
    sys.exit(1)

content = json.loads(response.content)
logging.info('Company name: {}'.format(content['dataset']['name']))

for data in content['dataset']['data']:
    print data[0], float(data[5])