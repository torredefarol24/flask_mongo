from flask import jsonify, request
from src.modules.prescription import controller
from src.main.app import app


@app.route("/api/v1/prescriptions", methods=['GET'])
def get_prescriptions_ep():
	resp = controller.get_prescriptions()
	return jsonify(resp["context"]), resp["status_code"]

@app.route("/api/v1/prescriptions/<id>", methods=['GET'])
def get_prescriptions_byId_ep(id):
	resp = controller.get_prescription_byId(id)
	return jsonify(resp["context"]), resp["status_code"]

@app.route("/api/v1/prescriptions", methods=['POST'])
def create_prescription_ep():
	resp = controller.create_prescription(request.json)
	return jsonify(resp["context"]), resp["status_code"]

@app.route("/api/v1.1/prescriptions", methods=['POST'])
def create_prescription_wmd_ep():
	resp = controller.create_prescription_wmd(request.json)
	return jsonify(resp["context"]), resp["status_code"]
