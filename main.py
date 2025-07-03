from auth import login
from create_entities import create_user, create_technician, create_sensor
from simulate_readings import send_bulk_readings
from create_tickets import create_ticket
from generate_reports import create_report
from config import SUPERADMIN, ADMIN, USER, TECH
from datetime import datetime
from metrics import ReportMetrics

# Logins
superadmin_token = login(SUPERADMIN["email"], SUPERADMIN["password"])
admin_token = login(ADMIN["email"], ADMIN["password"])
user_token = login(USER["email"], USER["password"])

# Crear usuarios y sensores
user = create_user(admin_token, "Test", "User", "testuser@client.com")
sensor = create_sensor(admin_token, user["id"], "SN-TEST-001")

# Simular lecturas
send_bulk_readings(user_token, sensor["id"], datetime.utcnow())

# Crear reporte
report = create_report(user_token, sensor["id"])
print("Reporte generado:", report)

# Crear alerta / ticket como usuario (si aplica tu flujo)
# alert = ...
# ticket = create_ticket(user_token, sensor["id"], alert["id"])
metrics = ReportMetrics()

# Generar reporte
report = create_report(user_token, sensor["id"], metrics)

# Descargarlo
content = download_report(user_token, report["id"], metrics)

# Ver métricas acumuladas
metrics.show()