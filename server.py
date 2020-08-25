from med_reminder.main.app import med_reminder_app
from med_reminder.bootstrap.logger import logger

if __name__ == '__main__':
      med_reminder_app.run(host='0.0.0.0')
      logger.info("MedReminder API Running")