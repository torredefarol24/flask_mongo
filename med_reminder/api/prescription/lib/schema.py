from med_reminder.bootstrap.mongo_conn import mdb
from med_reminder.api.user.lib.schema import UserSchema
from med_reminder.api.dosage.lib.schema import DosageSchema
# from med_reminder.api.dosage.lib.schema import DosageEmbDocSchema as Dosage_EmbDocSch

class PrescriptionSchema(mdb.Document):
      user = mdb.ReferenceField(UserSchema)
      # dosages = mdb.ListField(mdb.EmbeddedDocumentField(Dosage_EmbDocSch))
      dosages = mdb.ListField(ReferenceField(DosageSchema))
      ongoing = mdb.BooleanField(default = True)
      created_at = mdb.DateTimeField(default = datetime.datetime.now())
      updated_at = mdb.DateTimeField(default = datetime.datetime.now())

      meta = {
            "collection" : "prescriptions"
      }