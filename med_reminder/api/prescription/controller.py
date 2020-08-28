from med_reminder.api.prescription.model import Prescription
from med_reminder.api.user.model import User
from med_reminder.api.dosage.model import Dosage
from med_reminder.api.medicine.model import Medicine
from med_reminder.utils.prepare_ctx import controller_resp
from med_reminder.utils.logger import logger
from bson.objectid import ObjectId

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
            return controller_resp(200, presc, "Prescription Fetched")
      except Exception as excp:
            logger.error('Prescription::get_prescriptions %s', excp)
            return controller_resp(500, None, "Something went wrong")

def create_prescription(data):
      try:
            user = User.get_by_id(data["user"])
            dose = Dosage.get_by_id(data["dosage"])
            created_presc = Prescription.create(user=user, dose=dose)
            return controller_resp(200, created_presc, "Prescription Created")
      except Exception as excp:
            logger.error('Prescription::create_prescription %s', excp)
            return controller_resp(500, None, "Something went wrong")

def create_prescription_wmd(data):
      try:
            user = User.get_by_id(data["user"])
            medicine = Medicine.create(data=data["medicine"])
            dosage = Dosage.create(data=data, med=medicine)
            comp_dosage = Dosage.set_enddate(dosage=dosage)
            created_presc = Prescription.create(user=user, dose=comp_dosage)
            return controller_resp(200, created_presc, "Prescription Created with Med & Dosage")
      except Exception as excp:
            logger.error('Prescription::create_prescription_wmd %s', excp)
            return controller_resp(500, None, "Something went wrong")
