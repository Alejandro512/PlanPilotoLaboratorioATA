import requests
from config import API_URL

def login(email, password):
    res = requests.post(f"{API_URL}/auth/login", json={"email": email, "password": password})
    res.raise_for_status()
    return res.json()["access_token"]
