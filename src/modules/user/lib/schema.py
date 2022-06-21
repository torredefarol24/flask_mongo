import datetime

from src.main.bootstrap.db import mdb


class UserSchema(mdb.Document):
	name = mdb.StringField(required=True, max_length=120)
	phone = mdb.StringField(required=True, max_length=16)
	age = mdb.IntField(max_mength=3)
	created_at = mdb.DateTimeField(default = datetime.datetime.now())
	updated_at = mdb.DateTimeField(default = datetime.datetime.now())

	meta = {
		"collection" : "users"
	}
