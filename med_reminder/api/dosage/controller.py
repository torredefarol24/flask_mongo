from med_reminder.api.dosage.model import Dosage
from med_reminder.api.medicine.model import Medicine
from med_reminder.utils.prepare_ctx import controller_resp
from med_reminder.utils.logger import logger

def get_dosages():
      try:
            dosages = Dosage.get()
            return controller_resp(200, dosages, "Dosages Fetched")
      except Exception as excp:
            logger.error('Dosage::get_dosage %s', excp)
            return controller_resp(500, None, "Something went wrong")

def get_dosage_byId(id):
      try:
            dosage = Dosage.get_by_id(id)
            return controller_resp(200, dosage, "Dosage Fetched")
      except Exception as excp:
            logger.error('Dosage::get_dosage %s', excp)
            return controller_resp(500, None, "Something went wrong")

def __getMed_create_dosage(med, dose_data):
      new_dosage = Dosage.create(data=dose_data, med=med)
      fin_dosage = Dosage.set_enddate(dosage=new_dosage)
      return fin_dosage

def create_dosage(data):
      try:
            found_med = Medicine.get_by_id(data["medicine"])
            created_dosage = __getMed_create_dosage(found_med, dose_data=data)
            return controller_resp(201, created_dosage, "Dosage Created")
      except Exception as excp:
            logger.error('Dosage::create_dosage %s', excp)
            return controller_resp(500, None, 'Something went wrong')

def create_medicine_dosage(data):
      try:
            new_medicine = Medicine.create(data=data["medicine"])
            created_dosage = __getMed_create_dosage(new_medicine, dose_data=data)
            return controller_resp(201, created_dosage, "Dosage & Medicine Created")
      except Exception as excp:
            logger.error('Dosage::create_dosage %s', excp)
            return controller_resp(500, None, 'Something went wrong')