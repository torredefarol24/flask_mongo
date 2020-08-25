from flask import Flask

med_reminder_app = Flask(__name__)

if __name__ == '__main__':
      # FOR DOCKER CONTAINER LATER
      # med_reminder_app.run(debug=False, host='0.0.0.0')

      # RUN SERVER
      med_reminder_app.run(debug=True, host='127.0.0.1', port=6000)