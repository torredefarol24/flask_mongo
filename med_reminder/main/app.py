# Initialize App
from flask import Flask
med_reminder_app = Flask(__name__)

# Connect to DB
# from med_reminder.bootstrap.db_connection import initialize_mdb
# dbconn = initialize_mdb(med_reminder_app)

# Bootstrap Setup
from med_reminder.bootstrap import route_setup

