from med_reminder.api.medicine.lib.schema import MedicineSchema as MedicineMDB
from med_reminder.api.medicine.lib.helpers import postsaved_df, presaved_df
from bson import ObjectId

class Medicine:

      def get():
            medicine_list = MedicineMDB.objects()
            return presaved_df(medicine_list)

      def get_by_id(id):
            medicine = MedicineMDB.objects(id=ObjectId(id)).first()
            return postsaved_df(medicine)

      def create(data):
            new_med = MedicineMDB(
                  name=data['name'],
                  group_name=data['group_name'],
                  med_type=data['med_type']
                  ).save()
            return postsaved_df(new_med)

      # def create_raw(data):
      #       return MedicineMDB(
      #             name=data['name'],
      #             group_name=data['group_name'],
      #             med_type=data['med_type']
      #             ).save()
            