from med_reminder.api.user.lib.helpers import format_obj as format_user_obj
from med_reminder.api.dosage.lib.helpers import format_obj as format_dosage_obj
import datetime

def format_obj(presc_obj):
      return {
            "id" : str(presc_obj["id"]),
            "user" : format_user_obj(presc_obj["user"]),
            "dosage" : format_dosage_obj(presc_obj["dosage"]),
            "ongoing" : presc_obj["ongoing"]
      }

def presaved_df(prescription_list):
      prescriptions = []
      for prescription in prescription_list:
            prescriptions.append(format_obj(prescription))
      return prescriptions

def postsaved_df(presc_dt):
      return format_obj(presc_dt)