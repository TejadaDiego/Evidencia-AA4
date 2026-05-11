from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# =========================================
# INICIAR SPARK
# =========================================

spark = SparkSession.builder \
    .appName("PMR-Batch") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("====================================")
print("✅ Spark iniciado correctamente")
print("====================================")

# =========================================
# LEER CSV PRINCIPAL
# =========================================

df = spark.read.csv(
    "data/pasajeros.csv",
    header=True,
    inferSchema=True
)

print("====================================")
print("✅ CSV cargado")
print("====================================")

# =========================================
# MOSTRAR ESQUEMA
# =========================================

print("====================================")
print("📌 ESQUEMA")
print("====================================")

df.printSchema()

# =========================================
# MOSTRAR DATOS
# =========================================

print("====================================")
print("📌 PRIMEROS REGISTROS")
print("====================================")

df.show(10, False)

# =========================================
# KPI 1 - TOTAL PASAJEROS
# =========================================

print("====================================")
print("📌 KPI 1 - TOTAL PASAJEROS")
print("====================================")

total_pasajeros = df.count()

print(f"Total pasajeros: {total_pasajeros}")

# =========================================
# KPI 2 - PASAJEROS PMR
# =========================================

print("====================================")
print("📌 KPI 2 - PASAJEROS PMR")
print("====================================")

kpi_pmr = df.groupBy(
    "tipo_pmr"
).count().orderBy(
    col("count").desc()
)

kpi_pmr.show()

# =========================================
# KPI 3 - PASAJEROS POR ESTACION
# =========================================

print("====================================")
print("📌 KPI 3 - PASAJEROS POR ESTACION")
print("====================================")

kpi_estaciones = df.groupBy(
    "estacion_salida"
).count().orderBy(
    col("count").desc()
)

kpi_estaciones.show()

# =========================================
# KPI 4 - HORAS MÁS USADAS
# =========================================

print("====================================")
print("📌 KPI 4 - HORAS MÁS USADAS")
print("====================================")

kpi_horas = df.groupBy(
    "hora"
).count().orderBy(
    col("count").desc()
)

kpi_horas.show()

# =========================================
# SPARK SQL
# =========================================

print("====================================")
print("📌 SPARK SQL")
print("====================================")

df.createOrReplaceTempView("pasajeros")

sql_resultado = spark.sql("""

SELECT
    estacion_salida,
    COUNT(*) AS total
FROM pasajeros
GROUP BY estacion_salida
ORDER BY total DESC

""")

sql_resultado.show()

# =========================================
# RDD
# =========================================

print("====================================")
print("📌 RDD")
print("====================================")

rdd = df.rdd

print(f"Total RDD: {rdd.count()}")

print("Primer registro RDD:")
print(rdd.first())

# =========================================
# EXPORTAR RESULTADOS
# =========================================

print("====================================")
print("📌 EXPORTANDO RESULTADOS")
print("====================================")

# EXPORTAR KPI ESTACIONES
kpi_estaciones.write.mode("overwrite").csv(
    "output/output_estaciones"
)

# EXPORTAR SQL
sql_resultado.write.mode("overwrite").json(
    "output/output_sql"
)

# EXPORTAR KPI PMR
kpi_pmr.write.mode("overwrite").json(
    "output/output_tipo"
)

print("====================================")
print("✅ RESULTADOS EXPORTADOS")
print("====================================")

# =========================================
# FINALIZAR
# =========================================

spark.stop()

print("====================================")
print("✅ PROCESAMIENTO FINALIZADO")
print("====================================")