import requests
from dotenv import load_dotenv
import os
import logging
logger=logging.getLogger(__name__)
load_dotenv()
API_KEY = os.getenv('COINGECKO_API_KEY')
def extract():
    base_url = 'https://api.coingecko.com/api/v3/simple/price'
    params={
        'ids': 'bitcoin,ethereum,binancecoin',
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }
    headers={
        'x-cg-demo-api-key': API_KEY
    }
    try:
        response = requests.get(url=base_url, params=params, headers=headers)
        response.raise_for_status()
        logger.info(f"Extracted data for {len(response.json())} coins")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to extract data: {e}")
        raise

#response = extract() #checking
#print(response) #checking

if __name__ == '__main__':
    raw_data=extract()
    print(raw_data)