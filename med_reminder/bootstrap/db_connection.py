from flask_mongoengine import MongoEngine
from med_reminder.cred_vals.db import DBURL
from med_reminder.utils.logger import logger
from med_reminder.main.app import med_reminder_app


med_reminder_app.config['MONGO_SETTINGS'] = {
      "db" : "med_reminder",
      "host" : "mongodb://localhost/med_reminder",
}   

mdb = MongoEngine()
mdb.init_app(med_reminder_app)

# def initialize_mdb(app):

      # try :
      #       db_connection = mdb.connection('server')
      # except :
      #       logger.error('Mongo Connection Issue %s', sys.exc_info()[0])
      #       sys.exit(1)
      
