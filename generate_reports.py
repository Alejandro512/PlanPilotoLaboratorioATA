from config import API_URL
import requests

def create_report(token, sensor_id, start_date, end_date):
    url = f"{API_URL}/reports/create"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "parameters": {
            "sensorId": sensor_id,
            "startDate": start_date,
            "endDate": end_date
        },
        "format": "pdf"
    }
    res = requests.post(url, json=body, headers=headers)
    res.raise_for_status()
    return res.json()

def download_report(token, report_id, metrics):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(f"{API_URL}/reports/download/{report_id}", headers=headers)
    res.raise_for_status()

    metrics.log_downloaded()
    return res.content
