def prepare_controller_resp(status_code, data, msg):
      controller_response = {
            "context" : {
                  "success" : True if status_code in (200, 201) else False,
                  "message" : msg,
                  "data" : data
            },
            "status_code" : status_code
      }

      return controller_response