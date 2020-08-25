# Initialize App
from flask import Flask
med_reminder_app = Flask(__name__)

# Bootstrap Setup
from med_reminder.bootstrap import route_setup

