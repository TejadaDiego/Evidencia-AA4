from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS  # 🔥 IMPORTANTE

app = Flask(__name__)
CORS(app)  # 🔥 HABILITA conexión con tu frontend

# conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["pmr_db"]
collection = db["estaciones"]

# 👉 ruta principal (evita 404)
@app.route("/")
def home():
    return "API PMR funcionando 🚀"

# 👉 endpoint real
@app.route("/estaciones", methods=["GET"])
def get_estaciones():
    data = []
    
    for doc in collection.find({}, {"_id": 0}):
        data.append(doc)

    return jsonify(data)

# 👉 ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)