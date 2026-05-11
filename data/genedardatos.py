import csv
import random

TOTAL_REGISTROS = 50000

estaciones = [
    "GAM", "JAR", "VMA", "SMA", "ANG",
    "UNI", "NAR", "MAT", "CUL", "PUE"
]

tipos_pmr = [
    "PMR_SILLA",
    "PMR_VISUAL",
    "PMR_ADULTO_MAYOR",
    "PMR_AUDITIVO"
]

horas = [
    "06:00", "07:00", "08:00", "09:00",
    "10:00", "11:00", "12:00", "13:00",
    "14:00", "15:00", "16:00", "17:00",
    "18:00", "19:00", "20:00"
]

with open("data/pasajeros.csv", mode="w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    writer.writerow([
        "id",
        "estacion_salida",
        "estacion_llegada",
        "tipo_pmr",
        "hora"
    ])

    for i in range(1, TOTAL_REGISTROS + 1):

        salida = random.choice(estaciones)

        llegada = random.choice(estaciones)

        while salida == llegada:
            llegada = random.choice(estaciones)

        tipo = random.choice(tipos_pmr)

        hora = random.choice(horas)

        writer.writerow([
            i,
            salida,
            llegada,
            tipo,
            hora
        ])

print("===================================")
print("✅ pasajeros.csv generado")
print(f"✅ Total registros: {TOTAL_REGISTROS}")
print("===================================")