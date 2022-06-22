from bson.objectid import ObjectId
from src.modules.dosage.model import Dosage
from src.modules.medicine.model import Medicine
from src.modules.prescription.model import Prescription
from src.modules.user.model import User
from src.utils.logger import logger
from src.utils.response import controller_resp


def get_prescriptions():
	try:
		prescriptions = Prescription.get()
		return controller_resp(200, prescriptions, "Prescriptions Fetched")
	except Exception as excp:
		logger.error('Prescription::get_prescriptions %s', excp)
		return controller_resp(500, None, "Something went wrong")

def get_prescription_byId(id):
	try:
		presc = Prescription.get_by_id(id)
		status_code = 200 if presc else 404
		message = "Prescription Fetched" if presc else "Prescription Not Found"
		return controller_resp(status_code, presc, message)
	except Exception as excp:
		logger.error('Prescription::get_prescriptions %s', excp)
		return controller_resp(500, None, "Something went wrong")

def create_prescription(data):
	try:
		user = User.get_by_id(data["user"])
		dose = Dosage.get_by_id(data["dosage"])
		if (not user or not dose):
			return controller_resp(404, {}, "Invalid User/Dosage")
		created_presc = Prescription.create(user=user, dose=dose)
		return controller_resp(200, created_presc, "Prescription Created")
	except Exception as excp:
		logger.error('Prescription::create_prescription %s', excp)
		return controller_resp(500, None, "Something went wrong")

def create_prescription_wmd(data):
	try:
		user = User.get_by_id(data["user"])
		if (not user):
			return controller_resp(404, {}, "User not found")
		medicine = Medicine.create(data=data["medicine"])
		dosage = Dosage.create(data=data, med=medicine)
		comp_dosage = Dosage.set_enddate(dosage=dosage)
		created_presc = Prescription.create(user=user, dose=comp_dosage)
		return controller_resp(200, created_presc, "Prescription Created with Med & Dosage")
	except Exception as excp:
		logger.error('Prescription::create_prescription_wmd %s', excp)
		return controller_resp(500, None, "Something went wrong")
