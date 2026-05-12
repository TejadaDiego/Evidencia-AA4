from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

# =========================================
# INICIAR FLASK
# =========================================

app = Flask(__name__)

CORS(app)

# =========================================
# CONEXION MONGODB
# =========================================

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["pmr_db"]

collection = db["kpi_estaciones"]

print("====================================")
print("✅ API conectada a MongoDB")
print("====================================")

# =========================================
# RUTA PRINCIPAL
# =========================================

@app.route("/")
def home():

    return jsonify({
        "mensaje": "API PMR funcionando 🚀"
    })

# =========================================
# ENDPOINT ESTACIONES
# =========================================

@app.route("/estaciones")
def estaciones():

    data = []

    for doc in collection.find({}, {"_id": 0}):

        data.append(doc)

    return jsonify(data)

# =========================================
# EJECUTAR API
# =========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5050,
        debug=True
    )