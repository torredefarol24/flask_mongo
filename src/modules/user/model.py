from bson import ObjectId
from src.modules.user.lib.helpers import postsaved_df, presaved_df
from src.modules.user.lib.schema import UserSchema as UserMDB


class User:

	def get():
		users_list = UserMDB.objects()
		return presaved_df(users_list)
	
	def get_by_id(id):
		user = UserMDB.objects(id=ObjectId(id)).first()
		return postsaved_df(user) if user else None

	def create(data):
		new_user = UserMDB(
			name=data['name'],
			phone=data['phone'],
			age=data['age']
			).save()
		return postsaved_df(new_user)
		