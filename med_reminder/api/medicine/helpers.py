from bson.objectid import ObjectId

def presaved_df(data):
      return  {
            "name" : data["name"],
            "user" : ObjectId(data["user_id"])
      }

def postsaved_df(data):
      return {
            'id' : str(data['_id']),
            'name' : str(data['name'])
      }