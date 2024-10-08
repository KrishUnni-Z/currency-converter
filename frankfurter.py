import requests

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    Returns a list of available currencies or None in case of error.
    """
    url = f"{BASE_URL}/currencies"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        currencies = response.json()
        return list(currencies.keys())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching currencies: {e}")
        return None

def get_latest_rates(from_currency, to_currency, amount):
    """
    Function to get the latest conversion rate between the provided currencies.
    Returns date and rate or None twice in case of error.
    """
    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rate = data['rates'][to_currency]
        date = data['date']
        return date, rate
    except requests.exceptions.RequestException as e:
        print(f"Error fetching conversion rate: {e}")
        return None, None

def get_historical_rate(from_currency, to_currency, from_date, amount):
    """
    Function to get the conversion rate for the given currencies and date.
    Returns the conversion rate or None in case of error.
    """
    url = f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates'][to_currency]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical rate: {e}")
        return None
