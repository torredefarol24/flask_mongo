from med_reminder.bootstrap.mongo_connection import mongo as mdb
from med_reminder.helpers.validate_required_fields import validate_fields
from med_reminder.api.medicine.helpers import postsaved_df, presaved_df

med_coll = mdb.db.medicines
required_fields = ['name', 'user_id']

class Medicine:

      def get():
            meds = []
            meds_list = med_coll.find()
            for med in meds_list:
                  meds.append(postsaved_df(med))
            return meds

      def create(data):
            validate_fields(data, required_fields)
            med_data = presaved_df(data)
            med_id = med_coll.insert(med_data)
            created_med = med_coll.find_one({ '_id' : med_id})
            qr = postsaved_df(created_med)
            return qr