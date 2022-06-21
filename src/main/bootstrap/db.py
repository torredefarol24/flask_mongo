from flask_mongoengine import MongoEngine
from src.main.app import app

mdb = MongoEngine()
app.config['MONGODB_SETTINGS'] = {
	'db': 'med_reminder',
	'host': '172.30.1.2',
	'port': 27017
}

conn = mdb.init_app(app)
print("DBCONN", conn)
