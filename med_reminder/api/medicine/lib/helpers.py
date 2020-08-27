from bson.objectid import ObjectId
from med_reminder.dicts.med_types import MED_KEYS

def med_embdoc_df(med_embdoc):
      return {
            "name" : med_embdoc["name"],
            "group_name" : med_embdoc["group_name"],
            "med_type_name" : MED_KEYS[med_embdoc["med_type"]]
      }

def format_obj(med_obj):
      return {
            "id" : str(ObjectId(med_obj["id"])),
            "name" : med_obj["name"],
            "group_name" : med_obj["group_name"],
            "med_type" :   MED_KEYS[med_obj['med_type']],
            "created_at" : med_obj['created_at'].isoformat()
      }

def presaved_df(med_list):
      meds = []
      for med in med_list:
            meds.append(format_obj(med))
      return meds

def postsaved_df(med_dt):
      return format_obj(med_dt)