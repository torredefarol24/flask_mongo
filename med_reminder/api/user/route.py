from flask import request, jsonify
from med_reminder.main.app import med_reminder_app
from med_reminder.api.user import controller 

@med_reminder_app.route("/api/v1/users", methods=['GET'])
def get_users_ep():
      resp = controller.get_users()
      return jsonify(resp["context"]), resp["status_code"] 

@med_reminder_app.route("/api/v1/users", methods=['POST'])
def create_user_ep():
      resp = controller.create_user(request.json)
      return jsonify(resp["context"]), resp["status_code"] 
