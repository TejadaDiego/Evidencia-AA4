import csv
import json
import random
from datetime import datetime, timedelta

# ==============================
# CONFIGURACIÓN
# ==============================

BASE_PATH = "/data/"  # 👈 CLAVE: todo se guarda aquí

estaciones = ["SMA", "MIG", "VMA", "MAU", "SCA", "JAR", "ATO", "GAM"]

tipos = [
    "PMR",
    "PMR_SILLA",
    "PMR_RAMPA",
    "INVIDENTE"
]

# ==============================
# CSV PRINCIPAL
# ==============================

with open(BASE_PATH + "pasajeros.csv", "w", newline="") as f:
    writer = csv.writer(f)
    
    # CABECERA LIMPIA (IMPORTANTE)
    writer.writerow(["id", "estacion_salida", "estacion_llegada", "tipo_pmr", "hora"])

    for i in range(1, 1201):
        writer.writerow([
            i,
            random.choice(estaciones),
            random.choice(estaciones),
            random.choice(tipos),
            (datetime.now() + timedelta(minutes=random.randint(0, 500))).strftime("%H:%M")
        ])

# ==============================
# estaciones.json
# ==============================

with open(BASE_PATH + "estaciones.json", "w") as f:
    json.dump([{"codigo": e} for e in estaciones], f, indent=4)

# ==============================
# personal.csv
# ==============================

with open(BASE_PATH + "personal.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "nombre"])
    for i in range(1, 51):
        writer.writerow([i, f"Empleado{i}"])

# ==============================
# horarios.json
# ==============================

with open(BASE_PATH + "horarios.json", "w") as f:
    json.dump(
        [{"tren": i, "hora": f"{6+i}:00"} for i in range(1, 21)],
        f,
        indent=4
    )

# ==============================
# eventos.txt
# ==============================

with open(BASE_PATH + "eventos.txt", "w") as f:
    for i in range(1, 1201):
        f.write(f"Evento {i}\n")

print("✔ Datos generados correctamente en /data")