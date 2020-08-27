from bson.objectid import ObjectId
from med_reminder.dicts.med_types import MED_KEYS
import datetime

def med_embdoc_df(med_embdoc):
      return {
            "name" : med_embdoc["name"],
            "group_name" : med_embdoc["group_name"],
            "med_type_name" : MED_KEYS[med_embdoc["med_type"]]
      }

def format_obj(dosage_obj):
      return {
            "id" : str(ObjectId(dosage_obj["id"])),
            "amount_bought" : dosage_obj["amount_bought"],
            "frequency" : dosage_obj["frequency"],
            "medicine" : {
                  "name" : dosage_obj["medicine"]["name"],
                  "group_name" : dosage_obj["medicine"]["group_name"],
                  "med_type_name" : dosage_obj["medicine"]["med_type_name"]
            },
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