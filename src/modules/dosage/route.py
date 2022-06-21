from flask import request
from src.modules.dosage import controller
from src.main.app import app
from src.utils.response import json_resp

@app.route("/api/v1/dosages", methods=['GET'])
def get_dosages_ep():
	resp = controller.get_dosages()
	return json_resp(resp)

@app.route("/api/v1/dosages/<id>", methods=['GET'])
def get_dosage_byId_ep(id):
	resp = controller.get_dosage_byId(id)
	return json_resp(resp)

@app.route("/api/v1/dosages", methods=['POST'])
def create_dosage_ep():
	resp = controller.create_dosage(request.json)
	return json_resp(resp)

@app.route("/api/v1.1/dosages", methods=['POST'])
def create_medicine_dosage_ep():
	resp = controller.create_medicine_dosage(request.json)
	return json_resp(resp)
