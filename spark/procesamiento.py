from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# =========================================
# INICIAR SPARK
# =========================================

spark = SparkSession.builder \
    .appName("PMR-Batch") \
    .getOrCreate()

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
# MOSTRAR ESTRUCTURA
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

df.show(10)

# =========================================
# KPI 1 - TOTAL PASAJEROS
# =========================================

print("====================================")
print("📌 KPI 1 - TOTAL PASAJEROS")
print("====================================")

print(df.count())

# =========================================
# KPI 2 - PASAJEROS PMR
# =========================================

print("====================================")
print("📌 KPI 2 - PASAJEROS PMR")
print("====================================")

df.groupBy("tipo_pmr").count().show()

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

print("Total RDD:")
print(rdd.count())

print("Primer registro RDD:")
print(rdd.first())

# =========================================
# EXPORTAR RESULTADOS
# =========================================

print("====================================")
print("📌 EXPORTANDO RESULTADOS")
print("====================================")

kpi_estaciones.write.mode("overwrite").csv(
    "output/output_estaciones"
)

sql_resultado.write.mode("overwrite").json(
    "output/output_sql"
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