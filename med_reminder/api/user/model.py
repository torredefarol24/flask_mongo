from med_reminder.api.user.schema import UserSchema as UserMDB
from med_reminder.api.user.helpers import postsaved_df, presaved_df

class User:

      def get():
            users_list = UserMDB.objects()
            users = presaved_df(users_list)
            return users

      def create(data):
            new_user = UserMDB(
                  name=data['name'],
                  phone=data['phone'],
                  age=data['age']
                  ).save()
            created_user = postsaved_df(new_user)
            return created_user
