from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

# =========================================
# APP
# =========================================

app = Flask(__name__)

CORS(app)

# =========================================
# MONGODB
# =========================================

client = MongoClient(
    "mongodb://mongodb:27017/"
)

db = client["pmr_db"]

collection = db["kpi_estaciones"]

print("====================================")
print("✅ API conectada a MongoDB")
print("====================================")

# =========================================
# HOME
# =========================================

@app.route("/")

def home():

    return jsonify({

        "mensaje": "API PMR funcionando 🚀"

    })

# =========================================
# ESTACIONES
# =========================================

@app.route("/estaciones", methods=["GET"])

def get_estaciones():

    data = []

    for doc in collection.find({}, {"_id": 0}):

        data.append(doc)

    return jsonify(data)

# =========================================
# KPI TOTAL
# =========================================

@app.route("/total", methods=["GET"])

def total_pasajeros():

    total = 0

    for doc in collection.find():

        total += int(
            doc["total_pasajeros"]
        )

    return jsonify({

        "total_pasajeros": total

    })

# =========================================
# RUN
# =========================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",
        port=5000,
        debug=True

    )