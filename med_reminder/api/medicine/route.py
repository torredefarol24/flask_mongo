from flask import request, jsonify
from med_reminder.main.app import med_reminder_app
from med_reminder.api.medicine import controller 

@med_reminder_app.route("/api/v1/medicine", methods=['GET'])
def get_med_ep():
      resp = controller.get_medicines()
      return jsonify(resp["context"]), resp["status_code"] 

@med_reminder_app.route("/api/v1/medicine", methods=['POST'])
def create_med_ep():
      resp = controller.create_medicine(request.json)
      return jsonify(resp["context"]), resp["status_code"] 
