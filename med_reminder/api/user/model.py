# from med_reminder.main.app import dbconn as mdb
from med_reminder.bootstrap.db_connection import mdb
# from flask_mongoengine import MongoEngine
# mdb = MongoEngine()

class UserMDB(mdb.Document):
      name = mdb.StringField(required=True)
      phone = mdb.StringField(required=True)

      meta = {'allow_inheritance': True}

      def create_user(data):
            pass

class User(UserMDB):
      def create_user(data):
            return User(name=data["name"], phone=data["phone"]).save()