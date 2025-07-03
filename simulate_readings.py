# simulate_readings.py
import requests
from datetime import datetime, timedelta
from config import API_URL
import time

def send_bulk_readings(token, sensor_id, start_time, intervals=10):
    """
    Envía varios bulks, cada uno con 6 lecturas (3 min simulados).
    `intervals` controla cuántos ciclos quieres.
    """
    headers = {"Authorization": f"Bearer {token}"}
    for interval in range(intervals):
        batch = []
        for i in range(6):
            timestamp = start_time + timedelta(minutes=3*interval) + timedelta(seconds=i*30)
            batch.append({
                "sensorId": sensor_id,
                "timestamp": timestamp.isoformat(),
                "value": 25 + i,  # Valor simulado
                "unit": "°C",
                "quality": "ok"
            })
        res = requests.post(f"{API_URL}/sensor_readings/bulk", json=batch, headers=headers)
        res.raise_for_status()
        print(f"[{interval+1}/{intervals}] Bulk enviado correctamente.")
        # Espera real opcional
        time.sleep(1)  # O omite para simular sin pausa real
