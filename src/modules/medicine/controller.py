from src.modules.medicine.model import Medicine
from src.utils.logger import logger
from src.utils.prepare_ctx import controller_resp


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
		return controller_resp(200, medicine, "Medicine Fetched")
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
