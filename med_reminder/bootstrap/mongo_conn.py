from flask_mongoengine import MongoEngine
from med_reminder.cred_vals.db import DBURL
from med_reminder.main.app import med_reminder_app

mdb = MongoEngine()
med_reminder_app.config['MONGODB_SETTINGS'] = {
    'host' : DBURL
}
mdb.init_app(med_reminder_app)