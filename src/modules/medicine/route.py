from flask import request
from src.modules.medicine import controller
from src.main.app import app
from src.utils.response import json_resp

@app.route("/api/v1/medicines", methods=['GET'])
def get_med_ep():
	resp = controller.get_medicines()
	return json_resp(resp)

@app.route("/api/v1/medicines", methods=['POST'])
def create_med_ep():
	resp = controller.create_medicine(request.json)
	return json_resp(resp)

@app.route("/api/v1/medicines/<id>", methods=["GET"])
def get_medicine_byId_ep(id):
	resp = controller.get_medicine_byId(id)
	return json_resp(resp)
