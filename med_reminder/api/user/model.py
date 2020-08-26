from med_reminder.bootstrap.mongo_connection import mongo as mdb
from med_reminder.helpers.validate_required_fields import validate_fields
from med_reminder.api.user.helpers import presaved_df, postsaved_df

user_coll = mdb.db.users
required_fields = ['name', 'phone', 'age']

class User:

      def get():
            users = [] 
            users_list = user_coll.find()
            for user in users_list:
                  users.append(postsaved_df(user))
            return users

      def create(data):
            validate_fields(data, required_fields)
            u_data = presaved_df(data)
            user_id = user_coll.insert(u_data)
            created_user = user_coll.find_one({ '_id' : user_id})
            qr = postsaved_df(created_user)
            return qr
            