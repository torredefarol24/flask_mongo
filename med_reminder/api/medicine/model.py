from med_reminder.api.medicine.schema import MedicineSchema as MedicineMDB
from med_reminder.api.medicine.helpers import postsaved_df, presaved_df

class Medicine:

      def get():
            medicine_list = MedicineMDB.objects()
            meds = presaved_df(medicine_list)
            return meds
            # return medicine_list

      def create(data):
            new_med = MedicineMDB(
                  name=data['name'],
                  group_name=data['group_name'],
                  med_type=data['med_type']
                  ).save()
            created_med = postsaved_df(new_med)
            return created_med
