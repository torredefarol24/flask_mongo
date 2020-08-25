from med_reminder.api.user.model import User
from med_reminder.utils.prepare_ctx import prepare_controller_resp
from med_reminder.utils.logger import logger

def get_users():
      try : 
            users = User.get()
            ctr_resp = prepare_controller_resp(200, users, "Users Fetched")
            return ctr_resp
      except Exception as excp : 
            logger.error('User::get_users %s', excp)
            ctr_resp = prepare_controller_resp(500, None, "Something Went Wrong")
            return ctr_resp

def create_user(data):
      try :
            User.validate_fields(data)
            new_user = User.create(data=data)
            ctr_resp = prepare_controller_resp(201, new_user, "User Created")
            return ctr_resp
      except Exception as excp : 
            logger.error('User::create_user %s', excp)
            ctr_resp = prepare_controller_resp(500, None, "Something Went Wrong")
            return ctr_resp