from flask_pymongo import PyMongo
from med_reminder.cred_vals.db import DBURL
from med_reminder.main.app import med_reminder_app

med_reminder_app.config["MONGO_URI"] = DBURL
mongo = PyMongo(med_reminder_app)