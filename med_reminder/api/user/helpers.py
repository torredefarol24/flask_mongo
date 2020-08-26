def presaved_df(data):
      return {
            "name" : str(data['name']),
            "phone" : str(data['phone']),
            "age" : int(data['age'])
      }

def postsaved_df(data):
      return {
            'id' : str(data['_id']),
            'name' : str(data['name']), 
            'phone' : str(data['phone']),
            'age' : int(data['age'])
      }