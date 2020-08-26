from med_reminder.api.medicine.model import Medicine
from med_reminder.utils.prepare_ctx import controller_resp
from med_reminder.utils.logger import logger
from mongoengine.queryset import NotUniqueError

def get_medicines():
      try : 
            medicines = Medicine.get()
            return controller_resp(200, medicines, "Medicines Fetched")
      except Exception as excp : 
            logger.error('Medicine::get_medicines %s', excp)
            return controller_resp(500, None, "Something Went Wrong")

def create_medicine(data):
      try :
            new_med = Medicine.create(data=data)
            return controller_resp(201, new_med, "Medicine Created")
      except NotUniqueError:
            logger.error('Medicine::create_medicine Medicine Name Taken' )
            return controller_resp(409, None, "Medicine Created Already")
      except Exception as excp : 
            logger.error('Medicine::create_medicine %s', excp)
            return controller_resp(500, None, "Something Went Wrong")