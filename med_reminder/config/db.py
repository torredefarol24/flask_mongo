from med_reminder.cred_vals.db import DBNAME, DBURL

class DBConfig(object):
      MONGO_SETTINGS = {
            "db" : DBNAME,
            "host" : DBURL
      }
