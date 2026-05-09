import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================================
# CREAR CARPETA GRAFICOS
# =========================================

os.makedirs("output/graficos", exist_ok=True)

# =========================================
# LEER RESULTADOS SPARK
# =========================================

df = pd.read_csv(
    "output/output_estaciones/part-00000*.csv",
    header=None
)

df.columns = [
    "estacion_salida",
    "total"
]

# =========================================
# GRAFICO 1
# PASAJEROS POR ESTACION
# =========================================

plt.figure(figsize=(10,6))

plt.bar(
    df["estacion_salida"],
    df["total"]
)

plt.title("Pasajeros por Estación")
plt.xlabel("Estación")
plt.ylabel("Cantidad")

plt.savefig(
    "output/graficos/pasajeros_por_estacion.png"
)

print("✅ Gráfico 1 generado")

# =========================================
# GRAFICO 2
# TOP ESTACIONES
# =========================================

top5 = df.sort_values(
    by="total",
    ascending=False
).head(5)

plt.figure(figsize=(10,6))

plt.bar(
    top5["estacion_salida"],
    top5["total"]
)

plt.title("Top 5 Estaciones")
plt.xlabel("Estación")
plt.ylabel("Cantidad")

plt.savefig(
    "output/graficos/top5_estaciones.png"
)

print("✅ Gráfico 2 generado")

# =========================================
# GRAFICO 3
# PIE CHART
# =========================================

plt.figure(figsize=(8,8))

plt.pie(
    df["total"],
    labels=df["estacion_salida"],
    autopct='%1.1f%%'
)

plt.title("Distribución de Pasajeros")

plt.savefig(
    "output/graficos/distribucion_pasajeros.png"
)

print("✅ Gráfico 3 generado")

print("====================================")
print("✅ TODOS LOS GRÁFICOS GENERADOS")
print("====================================")