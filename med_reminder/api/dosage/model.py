from med_reminder.api.dosage.lib.schema import DosageSchema as DosageMDB
from med_reminder.api.medicine.lib.schema import MedicineSchema as MedicineMDB
from med_reminder.api.dosage.lib.helpers import presaved_df, postsaved_df, med_embdoc_df, tentative_end_date
from bson.objectid import ObjectId

class Dosage:

      def get():
            dosage_list = DosageMDB.objects()
            return presaved_df(dosage_list)

      def create(data):
            medicine_doc = MedicineMDB.objects(id=ObjectId(data["medicine"])).first()
            emb_med_doc = med_embdoc_df(medicine_doc)

            new_dosage = DosageMDB(
                  medicine = emb_med_doc,
                  amount_bought = data['amount_bought'],
                  frequency = data['frequency'],
                  quantity = data['quantity']
            ).save()

            end_date = tentative_end_date(new_dosage)
            DosageMDB.objects(id= ObjectId(new_dosage["id"])).update_one(set__dose_end_date=end_date)
            new_dosage["dose_end_date"] = end_date

            return postsaved_df(new_dosage)

