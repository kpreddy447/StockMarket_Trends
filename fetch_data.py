import requests
import logging

logging.basicConfig(filename='logfile/stocks_log_file.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def fetch_data(api_url, params):
    # Requesting data
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the status code is not 200
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None