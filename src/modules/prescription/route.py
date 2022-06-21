from flask import request
from src.modules.prescription import controller
from src.main.app import app
from src.utils.response import json_resp

@app.route("/api/v1/prescriptions", methods=['GET'])
def get_prescriptions_ep():
	resp = controller.get_prescriptions()
	return json_resp(resp)

@app.route("/api/v1/prescriptions/<id>", methods=['GET'])
def get_prescriptions_byId_ep(id):
	resp = controller.get_prescription_byId(id)
	return json_resp(resp)

@app.route("/api/v1/prescriptions", methods=['POST'])
def create_prescription_ep():
	resp = controller.create_prescription(request.json)
	return json_resp(resp)

@app.route("/api/v1.1/prescriptions", methods=['POST'])
def create_prescription_wmd_ep():
	resp = controller.create_prescription_wmd(request.json)
	return json_resp(resp)
