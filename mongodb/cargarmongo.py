from pymongo import MongoClient
import pandas as pd
import glob

# =========================================
# CONEXION MONGODB
# =========================================

client = MongoClient("mongodb://localhost:27017/")

db = client["pmr_db"]

print("====================================")
print("✅ Conectado a MongoDB")
print("====================================")

# =========================================
# LEER CSV RESULTADO SPARK
# =========================================

archivo = glob.glob(
    "output/output_estaciones/part*.csv"
)[0]

df = pd.read_csv(
    archivo,
    header=None
)

df.columns = [
    "estacion_salida",
    "total_pasajeros"
]

print(df.head())

# =========================================
# CONVERTIR A JSON
# =========================================

data = df.to_dict(
    orient="records"
)

# =========================================
# CREAR COLECCION
# =========================================

collection = db["kpi_estaciones"]

# limpiar colección anterior
collection.delete_many({})

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