from src.config.med_types import MED_KEYS


def format_obj(med_obj):
	return {
		"id" : str(med_obj["id"]),
		"name" : med_obj["name"],
		"group_name" : med_obj["group_name"],
		"med_type" :   MED_KEYS[med_obj['med_type']],
	}

def presaved_df(med_list):
	meds = []
	for med in med_list:
		meds.append(format_obj(med))
	return meds

def postsaved_df(med_dt):
	return format_obj(med_dt)
