from med_reminder.api.dosage.model import Dosage
from med_reminder.utils.prepare_ctx import controller_resp
from med_reminder.utils.logger import logger

def get_dosages():
      try:
            dosages = Dosage.get()
            return controller_resp(200, dosages, "Dosages Fetched")
      except Exception as excp:
            logger.error('Dosage::get_dosage %s', excp)
            return controller_resp(500, None, "Something went wrong")

def create_dosage(data):
      try:
            new_dosage = Dosage.create(data=data)
            return controller_resp(201, new_dosage, "Dosage Created")
      except Exception as excp:
            logger.error('Dosage::create_dosage %s', excp)
            return controller_resp(500, None, 'Something went wrong')

