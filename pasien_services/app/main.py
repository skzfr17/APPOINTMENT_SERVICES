# pasien_services/app/main.py
from flask import Flask, request, jsonify, abort
from database import get_db
from crud import create_pasien, get_pasien, get_pasien_by_id, update_pasien, delete_pasien
from sqlalchemy.orm import Session
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from models import Pasien

app = Flask(__name__)
CORS(app) 

@app.route("/pasien/", methods=["POST"])
def add_pasien():
    data = request.get_json()  # Mengambil data JSON dari request
    name_pasien = data.get("name_pasien")
    alamat = data.get("alamat")
    jenis_kelamin = data.get("jenis_kelamin")
    diagnosa = data.get("diagnosa")

    if not name_pasien or not alamat or not jenis_kelamin or not diagnosa:
        abort(400, description="Missing data")

    db = next(get_db())  # Mengambil sesi dari database
    new_pasien = create_pasien(db, name_pasien, alamat, jenis_kelamin, diagnosa)
    return jsonify(new_pasien.to_dict()), 201

@app.route("/pasien/", methods=["GET"])
def read_pasien():
    db = next(get_db())  # Mengambil sesi dari database
    pasien = get_pasien(db)
    return jsonify([p.to_dict() for p in pasien])

@app.route("/pasien/<int:pasien_id>", methods=["GET"])
def read_pasien_by_id(pasien_id):
    db = next(get_db())  # Mengambil sesi dari database
    pasien = get_pasien_by_id(db, pasien_id)
    if not pasien:
        abort(404, description="Pasien not found")
    return jsonify(pasien.to_dict())

@app.route("/pasien/<int:pasien_id>", methods=["PUT"])
def update_pasien_info(pasien_id):
    data = request.get_json()  # Mengambil data JSON dari request
    name_pasien = data.get("name_pasien")
    alamat = data.get("alamat")
    jenis_kelamin = data.get("jenis_kelamin")
    diagnosa = data.get("diagnosa")

    db = next(get_db())  # Mengambil sesi dari database
    updated_pasien = update_pasien(db, pasien_id, name_pasien, alamat, jenis_kelamin, diagnosa)
    if not updated_pasien:
        abort(404, description="Pasien not found")
    return jsonify(updated_pasien.to_dict())

@app.route("/pasien/<int:pasien_id>", methods=["DELETE"])
def delete_pasien_info(pasien_id):
    db = next(get_db())  # Mengambil sesi dari database
    success = delete_pasien(db, pasien_id)
    if not success:
        abort(404, description="Pasien not found")
    return jsonify({"message": "Pasien deleted successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
