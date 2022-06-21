from bson.objectid import ObjectId
from src.modules.dosage.lib.helpers import (postsaved_df, presaved_df,
                                                 tentative_end_date)
from src.modules.dosage.lib.schema import DosageSchema as DosageMDB


class Dosage:
 
	def get():
		dosage_list = DosageMDB.objects()
		return presaved_df(dosage_list)

	def get_by_id(id):
		dosage = DosageMDB.objects(id=ObjectId(id)).first()
		return postsaved_df(dosage)

	def create(data, med):
		new_dosage = DosageMDB(
			medicine = ObjectId(med["id"]),
			amount_bought = data['amount_bought'],
			frequency = data['frequency'],
			quantity = data['quantity']
		).save()
		return new_dosage

	def set_enddate(dosage):
		end_date = tentative_end_date(dosage)
		DosageMDB.objects(id= ObjectId(dosage["id"])).update_one(set__dose_end_date=end_date)
		dosage["dose_end_date"] = end_date
		return postsaved_df(dosage)
