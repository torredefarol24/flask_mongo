from med_reminder.bootstrap.mongo_conn import mdb
import datetime

class UserSchema(mdb.Document):
      name = mdb.StringField(required=True, max_length=120)
      phone = mdb.StringField(required=True, max_length=16)
      age = mdb.IntField(required=True, max_mength=3)
      created_at = mdb.DateTimeField(default = datetime.datetime.now())
      updated_at = mdb.DateTimeField(default = datetime.datetime.now())

      meta = {
            "collection" : "users"
      }