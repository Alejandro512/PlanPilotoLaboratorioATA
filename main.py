# main.py
from auth import login
from create_entities import create_user, create_sensor
from simulate_readings import send_bulk_readings
from generate_reports import create_report, download_report
from config import SUPERADMIN, ADMIN
from datetime import datetime
from metrics import ReportMetrics
import time

# Logins
superadmin_token = login(SUPERADMIN["email"], SUPERADMIN["password"])
admin_token = login(ADMIN["email"], ADMIN["password"])

# Inicializar métricas SOLO para reportes
metrics = ReportMetrics()

# ⚡ Configuración del plan piloto
NUM_USERS = 10
NUM_SENSORS_PER_USER = 10
NUM_REPORTS_PER_SENSOR = 3

# Bucle principal: crear usuarios, sensores, lecturas y reportes
for i in range(NUM_USERS):
    # ✅ Correo dinámico con timestamp para evitar colisiones
    timestamp = int(time.time())
    user_email = f"testuser{i}_{timestamp}@client.com"
    user_password = "user1234"  # o dinámico: f"userpass{i}" si quieres claves únicas

    # Crear usuario con correo único
    user = create_user(admin_token, "Test", f"User{i}", user_email, user_password)

    # Login usando esa misma clave
    user_token = login(user_email, user_password)

    for j in range(NUM_SENSORS_PER_USER):
        sensor_name = f"SN-TEST-{i}-{j}"
        sensor = create_sensor(admin_token, user["id"], sensor_name)

        # Simular lecturas para este sensor (5 ciclos de bulk inserts de ejemplo)
        send_bulk_readings(user_token, sensor["id"], datetime.utcnow(), intervals=5)

        # Crear múltiples reportes por sensor
        for k in range(NUM_REPORTS_PER_SENSOR):
            report = create_report(user_token, sensor["id"], metrics)
            print(f"Reporte generado: {report}")

            # Descargar el reporte para medir descarga
            content = download_report(user_token, report["id"], metrics)

# Mostrar métricas finales
metrics.show()
