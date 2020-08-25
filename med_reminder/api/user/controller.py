from med_reminder.api.user.model import User
from med_reminder.utils.prepare_ctx import prepare_controller_resp

def get_users():
      try : 
            users = User.objects()
            ctr_resp = prepare_controller_resp(200, users, "Users Fetched")
            return ctr_resp
      except Exception as excp : 
            ctr_resp = prepare_controller_resp(500, None, "Something Went Wrong")
            return ctr_resp

def create_user(data):
      try :
            # user = User(name=data["name"], phone=data['phone']).save()
            user = User.create_user(data)
            ctr_resp = prepare_controller_resp(201, user, "User Created")
            return ctr_resp
      except Exception as excp : 
            print(excp)
            ctr_resp = prepare_controller_resp(500, None, "Something Went Wrong")
            return ctr_resp