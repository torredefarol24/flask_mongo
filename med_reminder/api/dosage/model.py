from med_reminder.api.dosage.lib.schema import DosageSchema as DosageMDB
from med_reminder.api.dosage.lib.helpers import presaved_df, postsaved_df, tentative_end_date
from med_reminder.api.medicine.lib.helpers import med_embdoc_df
from bson.objectid import ObjectId

class Dosage:
 
      def get():
            dosage_list = DosageMDB.objects()
            return presaved_df(dosage_list)

      def create_dosage(data, med):
            emb_med_doc = med_embdoc_df(med)
            new_dosage = DosageMDB(
                  medicine = emb_med_doc,
                  amount_bought = data['amount_bought'],
                  frequency = data['frequency'],
                  quantity = data['quantity']
            ).save()
            return new_dosage

      def set_dosage_enddate(dosage):
            end_date = tentative_end_date(dosage)
            DosageMDB.objects(id= ObjectId(dosage["id"])).update_one(set__dose_end_date=end_date)
            dosage["dose_end_date"] = end_date
            return postsaved_df(dosage)