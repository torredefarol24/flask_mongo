from med_reminder.bootstrap.mongo_conn import mdb
from med_reminder.api.user.lib.schema import UserSchema
from med_reminder.api.dosage.lib.schema import DosageSchema
import datetime

class PrescriptionSchema(mdb.Document):
      user = mdb.ReferenceField(UserSchema)
      dosage = mdb.ReferenceField(DosageSchema)
      ongoing = mdb.BooleanField(default = True)
      created_at = mdb.DateTimeField(default = datetime.datetime.now())
      updated_at = mdb.DateTimeField(default = datetime.datetime.now())

      meta = {
            "collection" : "prescriptions"
      }