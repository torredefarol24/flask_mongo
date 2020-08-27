from med_reminder.api.user.lib.schema import UserSchema as UserMDB
from med_reminder.api.user.lib.helpers import postsaved_df, presaved_df

class User:

      def get():
            users_list = UserMDB.objects()
            return presaved_df(users_list)
            
      def create(data):
            new_user = UserMDB(
                  name=data['name'],
                  phone=data['phone'],
                  age=data['age']
                  ).save()
            return postsaved_df(new_user)
            