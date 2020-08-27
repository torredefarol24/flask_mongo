from med_reminder.bootstrap.mongo_conn import mdb
from med_reminder.api.medicine.lib.schema import MedicineEmbDocSchema as Med_EmbDocSch
import datetime

class DosageSchema(mdb.Document):
      medicine = mdb.EmbeddedDocumentField(Med_EmbDocSch)
      amount_bought = mdb.IntField(required=True)
      frequency = mdb.IntField(required=True)
      quantity = mdb.IntField(required=True)
      dose_start_date = mdb.DateTimeField(default = datetime.datetime.now())
      dose_end_date = mdb.DateTimeField()
      created_at = mdb.DateTimeField(default = datetime.datetime.now())
      updated_at = mdb.DateTimeField(default = datetime.datetime.now())

      meta = {
            "collection" : "dosages"
      }