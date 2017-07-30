import os
from pprint import pprint
import requests

TRANSPORT_API_APPLICATION_ID = os.environ['TRANSPORT_API_APPLICATION_ID']
TRANSPORT_API_APPLICATION_KEYS = os.environ['TRANSPORT_API_APPLICATION_KEYS']
TRANSPORT_API_DOMAIN = "https://transportapi.com/v3/"

def query_transport_api(service, date, time):
    """Query the

    Args:
        service (str): The service reference to the service of interest.
        date (str): The date of interest in yyyy-mm-dd format.
        time (str): The time of interest in hh:mm format.
    """
    url = "{0}uk/train/service/{1}/{2}/{3}/timetable.json?app_id={4}&app_key={5}&darwin=true&live=true".format(
        TRANSPORT_API_DOMAIN,
        service,
        date,
        time,
        TRANSPORT_API_APPLICATION_ID,
        TRANSPORT_API_APPLICATION_KEYS
    )

    data = requests.get(url).json()
    return pprint(data)

query_transport_api('25370002', '2017-07-25', '06:20')
