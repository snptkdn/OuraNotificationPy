import requests
from dotenv import load_dotenv
import os
from datetime import date

def get_sleep_data(oura_token: str, start_date:date=None, end_date: date=None) -> list:
    '''return ouraring's sleep data.

    Note! don't set same date start date and end date.

    Args:   
        oura_token(str): set token of oura api.
        start_date(date): set start date. (default is today-1)
        end_date(date): set end_date. (default is today)

    Returns:
        [json]: return list of sleep json data. 
    '''
    sleep_api = "{}{}".format(BASE_URL, "sleep")
    headers = { 
      'Authorization': 'Bearer {}'.format(OURA_TOKEN) 
    }

    response = requests.request('GET', sleep_api, headers=headers) 

    return response.json()['data']

def is_low_battery(oura_token: str, start_date: date=None, end_date: date=None):
    '''return ouraring has been low battery while date.

    Note! don't set same date start date and end date.

    Args:   
        oura_token(str): set token of oura api.
        start_date(date): set start date. (default is today-1)
        end_date(date): set end_date. (default is today)

    Returns:
        bool: ouraring has been low battery.
    '''

    sleep_data = get_sleep_data(
        oura_token,
        start_date=start_date,
        end_date=end_date
    )

    return any(
        [
            data['low_battery_alert']
            for data in sleep_data
        ]
    )

    
load_dotenv()
OURA_TOKEN = os.getenv('OURA_TOKEN')
BASE_URL = "https://api.ouraring.com/v2/usercollection/"
print(is_low_battery(OURA_TOKEN))


