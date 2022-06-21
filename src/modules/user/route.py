from flask import jsonify, request
from src.modules.user import controller
from src.main.app import app


@app.route("/api/v1/users", methods=['GET'])
def get_users_ep():
	resp = controller.get_users()
	return jsonify(resp["context"]), resp["status_code"] 

@app.route("/api/v1/users", methods=['POST'])
def create_user_ep():
	resp = controller.create_user(request.json)
	return jsonify(resp["context"]), resp["status_code"] 

@app.route("/api/v1/users/<id>", methods=["GET"])
def get_user_byId_ep(id):
	resp = controller.get_user_byId(id)
	return jsonify(resp["context"]), resp["status_code"]
