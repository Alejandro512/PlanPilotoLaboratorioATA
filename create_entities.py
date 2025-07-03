import requests
from config import API_URL

def create_user(token, name, lastname, email, password):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post(
        f"{API_URL}/users/create",
        json={
            "name": name,
            "lastname": lastname,
            "email": email,
            "company": "Prueba S.A.",
            "password": password  # <-- usa la variable
        },
        headers=headers
    )
    res.raise_for_status()
    return res.json()

def create_technician(token, name, lastname, email):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post(
        f"{API_URL}/technicians/create",
        json={
            "name": name,
            "lastname": lastname,
            "email": email,
            "phone": "+59312345678",
            "password": "tech1234"
        },
        headers=headers
    )
    res.raise_for_status()
    return res.json()

def create_sensor(token, user_id, serial):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post(
        f"{API_URL}/sensors/create_by_admin",
        json={
            "serial": serial,
            "type": "temperature",
            "location": "Lab Quito",
            "thresholds": {"min": 5, "max": 50},
            "ownerUserId": user_id
        },
        headers=headers
    )
    res.raise_for_status()
    return res.json()
