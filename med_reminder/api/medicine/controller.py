from med_reminder.api.medicine.model import Medicine
from med_reminder.utils.prepare_ctx import prepare_controller_resp
from med_reminder.utils.logger import logger

def get_medicines():
      try : 
            medicines = Medicine.get()
            ctr_resp = prepare_controller_resp(200, medicines, "Medicines Fetched")
            return ctr_resp
      except Exception as excp : 
            logger.error('Medicine::get_medicines %s', excp)
            ctr_resp = prepare_controller_resp(500, None, "Something Went Wrong")
            return ctr_resp

def create_medicine(data):
      try :
            new_med = Medicine.create(data=data)
            ctr_resp = prepare_controller_resp(201, new_med, "Medicine Created")
            return ctr_resp
      except Exception as excp : 
            logger.error('Medicine::create_medicine %s', excp)
            ctr_resp = prepare_controller_resp(500, None, "Something Went Wrong")
            return ctr_resp