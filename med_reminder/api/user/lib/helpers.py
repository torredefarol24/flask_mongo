def format_obj(u_obj):
      return {
            "id" : str(u_obj["id"]),
            "name" : u_obj["name"],
            "phone" : u_obj["phone"],
            "age" : u_obj['age']
      }

def presaved_df(user_list):
      users = []
      for user in user_list:
            users.append(format_obj(user))
      return users

def postsaved_df(user_dt):
      return format_obj(user_dt)