def get_dummy_test():
      context = {
            "success" : True,
            "message" : "GET DUMMY SUCCESSFULL",
            "data" : [1,4,2]
      }

      return {
            "context" : context,
            "status_code" : 200
      }
      
def create_dummy_test():
      print("CREATE DUMMY")
      context = {
            "success" : True,
            "message" : "CREATE DUMMY SUCCESSFULL",
            "data" : {}
      }
      return jsonify(context), 201
      


