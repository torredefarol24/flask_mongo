from src.modules.user.model import User
from src.utils.logger import logger
from src.utils.prepare_ctx import controller_resp


def get_users():
	try: 
		users = User.get()
		return controller_resp(200, users, "Users Fetched")            
	except Exception as excp : 
		logger.error('User::get_users %s', excp)
		return controller_resp(500, None, "Something Went Wrong")

def get_user_byId(id):
	try:
		user = User.get_by_id(id)
		return controller_resp(200, user, "User Fetched")
	except Exception as excp : 
		logger.error('User::get_user_byId %s', excp)
		return controller_resp(500, None, "Something Went Wrong")

def create_user(data):
	try:
		new_user = User.create(data=data)
		return controller_resp(201, new_user, "User Created")
	except Exception as excp : 
		logger.error('User::create_user %s', excp)
		return controller_resp(500, None, "Something Went Wrong")

