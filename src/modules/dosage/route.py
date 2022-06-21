from flask import jsonify, request
from src.modules.dosage import controller
from src.main.app import app


@app.route("/api/v1/dosages", methods=['GET'])
def get_dosages_ep():
	resp = controller.get_dosages()
	return jsonify(resp["context"]), resp["status_code"]

@app.route("/api/v1/dosages/<id>", methods=['GET'])
def get_dosage_byId_ep(id):
	resp = controller.get_dosage_byId(id)
	return jsonify(resp["context"]), resp["status_code"]

@app.route("/api/v1/dosages", methods=['POST'])
def create_dosage_ep():
	resp = controller.create_dosage(request.json)
	return jsonify(resp["context"]), resp["status_code"]

@app.route("/api/v1.1/dosages", methods=['POST'])
def create_medicine_dosage_ep():
	resp = controller.create_medicine_dosage(request.json)
	return jsonify(resp["context"]), resp["status_code"]
