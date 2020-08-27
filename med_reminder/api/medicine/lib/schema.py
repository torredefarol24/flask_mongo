from med_reminder.bootstrap.mongo_conn import mdb
import datetime

class MedicineSchema(mdb.Document):
      name = mdb.StringField(required=True, max_length=120)
      group_name = mdb.StringField(max_length=120)
      med_type = mdb.IntField(max_length=20)
      created_at = mdb.DateTimeField(default = datetime.datetime.now())
      updated_at = mdb.DateTimeField(default = datetime.datetime.now())

      meta = {
            "collection" : "medicines"
      }