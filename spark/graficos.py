import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

# =========================================
# CREAR CARPETA GRAFICOS
# =========================================

os.makedirs(
    "output/graficos",
    exist_ok=True
)

# =========================================
# LEER CSV SPARK
# =========================================

archivo = glob.glob(
    "output/output_estaciones/part*.csv"
)[0]

df = pd.read_csv(
    archivo,
    header=None
)

df.columns = [
    "estacion",
    "total"
]

print("====================================")
print("✅ DATAFRAME CARGADO")
print("====================================")

print(df)

# =========================================
# GRAFICO BARRAS
# =========================================

plt.figure(figsize=(10,6))

plt.bar(
    df["estacion"],
    df["total"]
)

plt.title(
    "Pasajeros por Estación"
)

plt.xlabel(
    "Estación"
)

plt.ylabel(
    "Total Pasajeros"
)

plt.savefig(
    "output/graficos/estaciones.png"
)

print("====================================")
print("✅ Grafico estaciones generado")
print("====================================")

# =========================================
# GRAFICO PIE
# =========================================

plt.figure(figsize=(8,8))

plt.pie(

    df["total"],

    labels=df["estacion"],

    autopct="%1.1f%%"

)

plt.title(
    "Distribución de Pasajeros"
)

plt.savefig(
    "output/graficos/distribucion.png"
)

print("====================================")
print("✅ Grafico distribucion generado")
print("====================================")