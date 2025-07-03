import requests
from datetime import datetime
from config import API_URL

def create_ticket(token, sensor_id, alert_id):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "sensorId": sensor_id,
        "issue": "Test issue",
        "subject": "Test subject",
        "description": "Test description",
        "priority": "high",
        "alertId": alert_id,
        "meeting": {
            "date": (datetime.utcnow() + timedelta(days=1)).isoformat(),
            "location": "https://meet.test.com"
        }
    }
    res = requests.post(f"{API_URL}/tickets/create", json=payload, headers=headers)
    res.raise_for_status()
    return res.json()
