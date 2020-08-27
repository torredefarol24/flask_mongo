from med_reminder.api.prescription.lib.schema import PrescriptionSchema as PrescriptionMDB
from med_reminder.api.prescription.lib.helpers import presaved_df, postsaved_df
from bson.objectid import ObjectId

class Prescription:
      def get():
            pres_list = PrescriptionMDB.objects()
            return presaved_df(pres_list)
      
      def get_by_id(id):
            presc = PrescriptionMDB.objects(id=ObjectId(id)).first()
            return postsaved_df(presc)

      def create(user, dose):
            created_pres = PrescriptionMDB(
                        user = ObjectId(user["id"]),
                        dosage = ObjectId(dose["id"])
                  ).save()
            return postsaved_df(created_pres)