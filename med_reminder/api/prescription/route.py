from flask import request, jsonify
from med_reminder.main.app import med_reminder_app
from med_reminder.api.prescription import controller

@med_reminder_app.route("/api/v1/prescriptions", methods=['GET'])
def get_prescriptions_ep():
      resp = controller.get_prescriptions()
      return jsonify(resp["context"]), resp["status_code"]

@med_reminder_app.route("/api/v1/prescriptions/<id>", methods=['GET'])
def get_prescriptions_byId_ep(id):
      resp = controller.get_prescription_byId(id)
      return jsonify(resp["context"]), resp["status_code"]

@med_reminder_app.route("/api/v1/prescriptions", methods=['POST'])
def create_prescription_ep():
      resp = controller.create_prescription(request.json)
      return jsonify(resp["context"]), resp["status_code"]

@med_reminder_app.route("/api/v1.1/prescriptions", methods=['POST'])
def create_prescription_wmd_ep():
      resp = controller.create_prescription_wmd(request.json)
      return jsonify(resp["context"]), resp["status_code"]