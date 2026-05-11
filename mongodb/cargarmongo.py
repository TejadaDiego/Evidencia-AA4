from pymongo import MongoClient
import pandas as pd
import glob
import os

# =========================================
# CONEXION MONGODB
# =========================================

client = MongoClient(
    "mongodb://mongodb:27017/"
)

db = client["pmr_db"]

print("====================================")
print("✅ Conectado a MongoDB")
print("====================================")

# =========================================
# BUSCAR ARCHIVO CSV SPARK
# =========================================

archivos = glob.glob(
    "output/output_estaciones/part*.csv"
)

if len(archivos) == 0:

    print("❌ No se encontró archivo CSV")
    exit()

archivo = archivos[0]

print("====================================")
print(f"📌 Archivo encontrado: {archivo}")
print("====================================")

# =========================================
# LEER CSV
# =========================================

df = pd.read_csv(
    archivo,
    header=None
)

# =========================================
# RENOMBRAR COLUMNAS
# =========================================

df.columns = [
    "estacion_salida",
    "total_pasajeros"
]

print("====================================")
print("📌 DATAFRAME")
print("====================================")

print(df.head())

# =========================================
# CONVERTIR A JSON
# =========================================

data = df.to_dict(
    orient="records"
)

# =========================================
# COLECCION
# =========================================

collection = db["kpi_estaciones"]

# limpiar colección anterior
collection.delete_many({})

print("====================================")
print("🗑️ Colección limpiada")
print("====================================")

# insertar nuevos documentos
collection.insert_many(data)

print("====================================")
print("✅ Datos insertados en MongoDB")
print("====================================")

# =========================================
# CONSULTA
# =========================================

print("====================================")
print("📌 CONSULTA MONGODB")
print("====================================")

for doc in collection.find({}, {"_id": 0}):

    print(doc)

print("====================================")
print("✅ FIN PROCESO MONGODB")
print("====================================")