from med_reminder.bootstrap.mongo_connection import mongo as mdb

user_coll = mdb.db.users
required_fields = ['name', 'phone']

class User:

      def validate_fields(data):
            for key in data:
                  if (key in required_fields):
                        continue
                  raise Exception("Required Keys Missing")
      
      def get():
            users = [] 
            users_list = user_coll.find()
            for user in users_list:
                  users.append({
                        'id' : str(user['_id']),
                        'name' : user['name'], 
                        'phone' : user['phone']
                  })
            return users

      def create(data):
            user_id = user_coll.insert(data)
            created_user = user_coll.find_one({ '_id' : user_id})
            qr = {
                  'id' : str(created_user['_id']),
                  'name' : created_user['name'], 
                  'phone' : created_user['phone']
            }
            return qr