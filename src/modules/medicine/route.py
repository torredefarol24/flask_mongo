from flask import jsonify, request
from src.modules.medicine import controller
from src.main.app import app


@app.route("/api/v1/medicines", methods=['GET'])
def get_med_ep():
	resp = controller.get_medicines()
	return jsonify(resp["context"]), resp["status_code"] 

@app.route("/api/v1/medicines", methods=['POST'])
def create_med_ep():
	resp = controller.create_medicine(request.json)
	return jsonify(resp["context"]), resp["status_code"] 

@app.route("/api/v1/medicines/<id>", methods=["GET"])
def get_medicine_byId_ep(id):
	resp = controller.get_medicine_byId(id)
	return jsonify(resp["context"]), resp["status_code"] 
