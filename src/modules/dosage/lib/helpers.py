import datetime

from src.modules.medicine.lib.helpers import format_obj as format_med_obj
from src.config.med_types import MED_KEYS


def format_obj(dosage_obj):
	return {
		"id" : str(dosage_obj["id"]),
		"amount_bought" : dosage_obj["amount_bought"],
		"frequency" : dosage_obj["frequency"],
		"medicine" : format_med_obj(dosage_obj["medicine"]),
		"quantity" : dosage_obj["quantity"],
		"dose_start_date" : dosage_obj["dose_start_date"].isoformat(),
		"dose_end_date" : dosage_obj["dose_end_date"].isoformat(),
		"created_at" : dosage_obj["created_at"].isoformat(),
	}

def presaved_df(dosage_list):
	dosages = []
	for dosage in dosage_list:
		dosages.append(format_obj(dosage))
	return dosages

def postsaved_df(dosage_dt):
	return format_obj(dosage_dt)

def tentative_end_date(dosage_dt):
	total_amount = dosage_dt["amount_bought"]
	frequency = dosage_dt["frequency"]
	dose_amount = dosage_dt["quantity"]
	dose_start_date = dosage_dt["dose_start_date"]

	days_to_last = total_amount / (frequency * dose_amount)
	med_end_date = dose_start_date + datetime.timedelta(days_to_last)

	return med_end_date
