import requests
import structs.structs as structs
import json

def make(url):
    try:
        response = requests.get(url, timeout=structs.REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error making request: {e}")

    try:
        return json.loads(response.text)
    except json.JSONDecodeError as e:
        raise Exception(f"Error parsing response: {e}")
