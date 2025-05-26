import requests
from .config import BACKEND_URL

def fetch_info_by_client():
    response = requests.get(f"{BACKEND_URL}/info-by-client")
    response.raise_for_status()
    return response.json()

def fetch_info_by_client_id(client_id):
    response = requests.get(f"{BACKEND_URL}/info-by-client", params={"client_id": client_id})
    response.raise_for_status()
    return response.json()

def fetch_all_transactions():
    response = requests.get(f"{BACKEND_URL}/")
    response.raise_for_status()
    return response.json()
