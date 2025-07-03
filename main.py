# main.py
from auth import login
from create_entities import create_user, create_sensor
from simulate_readings import send_bulk_readings
from generate_reports import create_report, download_report
from config import SUPERADMIN, ADMIN, USER
from datetime import datetime
from metrics import ReportMetrics

# Logins
superadmin_token = login(SUPERADMIN["email"], SUPERADMIN["password"])
admin_token = login(ADMIN["email"], ADMIN["password"])
user_token = login(USER["email"], USER["password"])

# Crear usuario y sensor
user = create_user(admin_token, "Test", "User", "testuser@client.com")
sensor = create_sensor(admin_token, user["id"], "SN-TEST-001")

# Simular lecturas
send_bulk_readings(user_token, sensor["id"], datetime.utcnow())

# Inicializar métricas SOLO para reportes
metrics = ReportMetrics()

# Crear reporte
report = create_report(user_token, sensor["id"], metrics)
print("Reporte generado:", report)

# Descargarlo
content = download_report(user_token, report["id"], metrics)

# Mostrar métricas finales
metrics.show()
