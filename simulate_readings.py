import requests
from datetime import datetime, timedelta
from config import API_URL

def send_bulk_readings(token, sensor_id, start_time):
    headers = {"Authorization": f"Bearer {token}"}
    batch = []
    for i in range(6):  # 6 lecturas de 30 seg => 3 min
        timestamp = start_time + timedelta(seconds=i*30)
        batch.append({
            "sensorId": sensor_id,
            "timestamp": timestamp.isoformat(),
            "value": 25 + i,  # Valor simulado
            "unit": "°C",
            "quality": "ok"
        })
    res = requests.post(f"{API_URL}/sensor_readings/bulk", json=batch, headers=headers)
    res.raise_for_status()
    return res.json()
