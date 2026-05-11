from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# =========================================
# INICIAR SPARK
# =========================================

spark = SparkSession.builder \
    .appName("PMR-Streaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("====================================")
print("✅ Spark Streaming iniciado")
print("====================================")

# =========================================
# LEER STREAM KAFKA
# =========================================

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:9092") \
    .option("subscribe", "pmr-events") \
    .option("startingOffsets", "earliest") \
    .load()

# =========================================
# CONVERTIR VALUE A STRING
# =========================================

df_string = df.selectExpr(
    "CAST(value AS STRING)"
)

# =========================================
# ESQUEMA JSON
# =========================================

schema = StructType([

    StructField(
        "evento_id",
        IntegerType()
    ),

    StructField(
        "tipo_evento",
        StringType()
    ),

    StructField(
        "estacion",
        StringType()
    ),

    StructField(
        "tipo_pmr",
        StringType()
    ),

    StructField(
        "minutos_retraso",
        IntegerType()
    )

])

# =========================================
# PARSE JSON
# =========================================

df_json = df_string.select(

    from_json(
        col("value"),
        schema
    ).alias("data")

)

df_final = df_json.select(
    "data.*"
)

# =========================================
# ALERTAS
# =========================================

alertas = df_final.filter(
    col("minutos_retraso") > 15
)

print("====================================")
print("✅ MOSTRANDO ALERTAS")
print("====================================")

# =========================================
# MOSTRAR STREAM
# =========================================

query = alertas.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()