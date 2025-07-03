from config import API_URL
import requests

def create_report(token, sensor_id, metrics):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "parameters": {
            "sensorId": sensor_id,
            "startDate": "2025-06-25T18:00:00Z",
            "endDate": "2025-06-25T20:00:00Z"
        },
        "format": "pdf"
    }
    res = requests.post(f"{API_URL}/reports/create", json=payload, headers=headers)
    res.raise_for_status()
    report = res.json()

    # 👉 Suponiendo que tu backend devuelve tamaño y contenedor
    size_mb = report.get("size_mb", 0.5)  # tamaño estimado si no lo envía
    container_id = report.get("container_id", "default")
    metrics.log_created(size_mb, container_id)

    return report

def download_report(token, report_id, metrics):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(f"{API_URL}/reports/download/{report_id}", headers=headers)
    res.raise_for_status()

    metrics.log_downloaded()
    return res.content
