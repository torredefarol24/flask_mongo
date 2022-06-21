import datetime

from src.modules.dosage.lib.schema import DosageSchema
from src.modules.user.lib.schema import UserSchema
from src.main.bootstrap.db import mdb


class PrescriptionSchema(mdb.Document):
	user = mdb.ReferenceField(UserSchema)
	dosage = mdb.ReferenceField(DosageSchema)
	ongoing = mdb.BooleanField(default = True)
	created_at = mdb.DateTimeField(default = datetime.datetime.now())
	updated_at = mdb.DateTimeField(default = datetime.datetime.now())

	meta = {
		"collection" : "prescriptions"
	}
