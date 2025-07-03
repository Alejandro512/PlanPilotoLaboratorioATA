from config import API_URL
import requests

def create_report(token, sensor_id, metrics, container_id=None):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "parameters": {
            "sensorId": sensor_id,
            "startDate": "2025-06-25T18:00:00Z",
            "endDate": "2025-06-25T20:00:00Z"
        },
        "format": "pdf"
    }

    # 👉 Si quieres que el backend lo reciba explícito:
    if container_id:
        payload["containerId"] = container_id

    res = requests.post(f"{API_URL}/reports/create", json=payload, headers=headers)
    res.raise_for_status()
    report = res.json()

    # 👉 Toma container_id del backend o usa el que enviaste
    size_mb = report.get("size_mb", 0.5)
    reported_container_id = report.get("container_id", container_id or "default")
    metrics.log_created(size_mb, reported_container_id)

    return report


def download_report(token, report_id, metrics):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(f"{API_URL}/reports/download/{report_id}", headers=headers)
    res.raise_for_status()

    metrics.log_downloaded()
    return res.content
