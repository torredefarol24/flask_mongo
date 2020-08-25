from flask import jsonify
from med_reminder.main.app import med_reminder_app
from med_reminder.api.dummy_test import controller 

@med_reminder_app.route("/api/v1/dummy", methods=['GET'])
def get_dummy_route():
      resp = controller.get_dummy_test()
      return jsonify(resp["context"]), resp["status_code"] 

@med_reminder_app.route("/api/v1/dummy", methods=['POST'])
def post_dummy_route():
      resp = controller.create_dummy_test()
      return jsonify(resp["context"]), resp["status_code"] 


