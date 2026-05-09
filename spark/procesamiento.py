from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("PMR-Proyecto").getOrCreate()

# ==============================
# CARGA DE DATOS
# ==============================

df = spark.read.csv("/data/pasajeros.csv", header=True, inferSchema=True)

print("=== DATOS INICIALES ===")
df.show(10)

# ==============================
# NORMALIZAR COLUMNAS (CLAVE)
# ==============================

# Convierte: "Tipo PMR" -> "tipo_pmr"
df = df.toDF(*[c.strip().lower().replace(" ", "_") for c in df.columns])

print("=== COLUMNAS NORMALIZADAS ===")
print(df.columns)

# ==============================
# VALIDACIÓN DE COLUMNAS
# ==============================

required_cols = ["tipo_pmr", "estacion_salida", "estacion_llegada"]

for col_name in required_cols:
    if col_name not in df.columns:
        raise Exception(f"❌ Falta la columna requerida: {col_name}")

# ==============================
# LIMPIEZA
# ==============================

df = df.dropna()

# ==============================
# ANALISIS
# ==============================

print("=== CANTIDAD POR TIPO PMR ===")
tipo_df = df.groupBy("tipo_pmr").count()
tipo_df.show()

print("=== DEMANDA POR ESTACION ===")
estaciones_df = df.groupBy("estacion_salida").count().orderBy(col("count").desc())
estaciones_df.show()

# ==============================
# SPARK SQL
# ==============================

df.createOrReplaceTempView("pmr")

resultado = spark.sql("""
SELECT estacion_llegada, COUNT(*) as total
FROM pmr
GROUP BY estacion_llegada
ORDER BY total DESC
""")

print("=== RESULTADO SQL ===")
resultado.show()

# ==============================
# GUARDAR RESULTADOS
# ==============================

tipo_df.write.mode("overwrite").json("/data/output_tipo")
estaciones_df.write.mode("overwrite").json("/data/output_estaciones")
resultado.write.mode("overwrite").json("/data/output_sql")

print("✔ Resultados guardados en /data/output_*")

# ==============================
# FINALIZAR
# ==============================

spark.stop()