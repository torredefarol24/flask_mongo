from src.modules.medicine.model import Medicine
from src.utils.logger import logger
from src.utils.response import controller_resp


def get_medicines():
	try : 
		medicines = Medicine.get()
		return controller_resp(200, medicines, "Medicines Fetched")
	except Exception as excp : 
		logger.error('Medicine::get_medicines %s', excp)
		return controller_resp(500, None, "Something Went Wrong")

def get_medicine_byId(id):
	try:
		medicine = Medicine.get_by_id(id)
		status_code = 200 if medicine else 404
		message = "Medicine Fetched" if medicine else "Medicine Not Found"
		return controller_resp(status_code, medicine, message)
	except Exception as excp : 
		logger.error('Medicine::get_medicine_byId %s', excp)
		return controller_resp(500, None, "Something Went Wrong")

def create_medicine(data):
	try :
		new_med = Medicine.create(data=data)
		return controller_resp(201, new_med, "Medicine Created")
	except Exception as excp : 
		logger.error('Medicine::create_medicine %s', excp)
		return controller_resp(500, None, "Something Went Wrong")
