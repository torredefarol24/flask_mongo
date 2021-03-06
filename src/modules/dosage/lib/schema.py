import datetime

from src.modules.medicine.lib.schema import MedicineSchema
from src.main.bootstrap.db import mdb


class DosageSchema(mdb.Document):
	medicine = mdb.ReferenceField(MedicineSchema)
	amount_bought = mdb.IntField(required=True)
	frequency = mdb.IntField(required=True)
	quantity = mdb.IntField(required=True)
	dose_start_date = mdb.DateTimeField(default = datetime.datetime.now())
	dose_end_date = mdb.DateTimeField()
	created_at = mdb.DateTimeField(default = datetime.datetime.now())
	updated_at = mdb.DateTimeField(default = datetime.datetime.now())

	meta = {
		"collection" : "dosages"
	}
