from med_reminder.api.medicine.model import Medicine
from med_reminder.utils.prepare_ctx import prepare_controller_resp
from med_reminder.utils.logger import logger
from mongoengine.queryset import NotUniqueError

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
      except NotUniqueError:
            logger.error('Medicine::create_medicine Medicine Name Taken' )
            ctr_resp = prepare_controller_resp(409, None, "Medicine Created Already")
            return ctr_resp
      except Exception as excp : 
            logger.error('Medicine::create_medicine %s', excp)
            print( excp["code"])
            ctr_resp = prepare_controller_resp(500, None, "Something Went Wrong")
            return ctr_resp