from kafka import KafkaProducer
import json
import random
import time

# ============================================
# CONEXIÓN A KAFKA
# ============================================

producer = KafkaProducer(
    bootstrap_servers='broker:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# ============================================
# DATOS BASE
# ============================================

estaciones = [
    "GAM",
    "JAR",
    "VMA",
    "SMA",
    "ANG",
    "UNI",
    "NAR"
]

tipos_pmr = [
    "PMR_SILLA",
    "PMR_VISUAL",
    "PMR_ADULTO_MAYOR",
    "PMR_AUDITIVO"
]

tipos_evento = [
    "retraso",
    "aglomeracion",
    "asistencia",
    "incidencia"
]

# ============================================
# ENVÍO DE EVENTOS
# ============================================

print("====================================")
print("✅ ENVIANDO EVENTOS A KAFKA")
print("====================================")

for i in range(1, 1001):

    evento = {

        "evento_id": i,

        "tipo_evento": random.choice(
            tipos_evento
        ),

        "estacion": random.choice(
            estaciones
        ),

        "tipo_pmr": random.choice(
            tipos_pmr
        ),

        "minutos_retraso": random.randint(
            0,
            30
        )
    }

    producer.send(
        "gestordetren",
        evento
    )

    producer.flush()

    print(evento)

    time.sleep(1)

print("====================================")
print("✅ EVENTOS FINALIZADOS")
print("====================================")