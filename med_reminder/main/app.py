from flask import Flask

# Initialize App
med_reminder_app = Flask(__name__)

# Bootstrap Setup
from med_reminder.bootstrap import route_setup

# from med_reminder.config.app_configs import AppConfig


