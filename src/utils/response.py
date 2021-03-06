from flask import jsonify


def controller_resp(status_code, data, msg):
	return {
		"context" : {
			"success" : True if status_code in (200, 201) else False,
			"message" : msg,
			"data" : data
		},
		"status_code" : status_code
	}

def json_resp(resp):
	return jsonify(resp["context"]), resp["status_code"]
