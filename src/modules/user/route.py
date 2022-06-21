from flask import request
from src.main.app import app
from src.modules.user import controller
from src.utils.response import json_resp


@app.route("/api/v1/users", methods=['GET'])
def get_users_ep():
	resp = controller.get_users()
	return json_resp(resp)

@app.route("/api/v1/users", methods=['POST'])
def create_user_ep():
	resp = controller.create_user(request.json)
	return json_resp(resp)

@app.route("/api/v1/users/<id>", methods=["GET"])
def get_user_byId_ep(id):
	resp = controller.get_user_byId(id)
	return json_resp(resp)
