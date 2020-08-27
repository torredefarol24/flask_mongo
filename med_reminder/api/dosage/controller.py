from med_reminder.api.dosage.model import Dosage
from med_reminder.api.medicine.model import Medicine
from med_reminder.api.medicine.lib.schema import MedicineSchema as MedicineMDB
from med_reminder.utils.prepare_ctx import controller_resp
from med_reminder.utils.logger import logger
from bson.objectid import ObjectId

def get_dosages():
      try:
            dosages = Dosage.get()
            return controller_resp(200, dosages, "Dosages Fetched")
      except Exception as excp:
            logger.error('Dosage::get_dosage %s', excp)
            return controller_resp(500, None, "Something went wrong")

def __getMed_create_dosage(med, dose_data):
      new_dosage = Dosage.create_dosage(data=dose_data, med=med)
      comp_dosage = Dosage.set_dosage_enddate(dosage=new_dosage)
      return comp_dosage

def create_dosage(data):
      try:
            found_med = MedicineMDB.objects(id=ObjectId(data["medicine"])).first()
            created_dosage = __getMed_create_dosage(found_med, dose_data=data)
            return controller_resp(201, created_dosage, "Dosage Created")
      except Exception as excp:
            logger.error('Dosage::create_dosage %s', excp)
            return controller_resp(500, None, 'Something went wrong')

def create_medicine_dosage(data):
      try:
            new_medicine = Medicine.create_raw(data=data["medicine"])
            created_dosage = __getMed_create_dosage(new_medicine, dose_data=data)
            return controller_resp(201, created_dosage, "Dosage & Medicine Created")
      except Exception as excp:
            logger.error('Dosage::create_dosage %s', excp)
            return controller_resp(500, None, 'Something went wrong')