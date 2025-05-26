from celery.schedules import crontab
from flask import current_app as app
from backend.celery.tasks import email_reminder

celery_app=app.extensions['celery']
#s-schedule task #every 10 seconds # sender.add_periodic_task(10.0,test.s('hello celery')) # sender.add_periodic_task(10.0,email_reminder.s('students@gmail','reminder to login','<h1>hello everyone</h1>')) #if functional parameters same in email reminders then name should be given to that particular object #daily message at 13:56pm everyday sender.add_periodic_task(crontab(hour=14,minute=8),email_reminder.s('students@gmail','reminder to login','<h1>hello everyone</h1>',name='daily reminder')) #weekly reminder sender.add_periodic_task(crontab(hour=14,minute=8,day_of_week='monday'),email_reminder.s('students@gmail','reminder to login','<h1>hello everyone</h1>'),name='weekly reminder') #monthly reminder sender.add_periodic_task(crontab(hour=14,minute=8,day_of_month='26'),email_reminder.s('students@gmail','reminder to login','<h1>hello everyone</h1>'),name='monthly reminder')

@celery_app.on_after_configure.connect
#sender is the current celery_app instance
def setup_periodic_tasks(sender, **kwargs):
    # every 10 seconds
    # sender.add_periodic_task(10.0, email_reminder.s('students@gmail', 'reminder to login', '<h1> hello everyone </h1>') )

    # daily message at 2:11 pm, everyday
    sender.add_periodic_task(crontab(hour=14, minute=11), email_reminder.s('students@gmail', 'reminder to login', '<h1> hello everyone </h1>'), name='daily reminder' )

    # weekly messages
    sender.add_periodic_task(crontab(hour=14, minute=11, day_of_week='monday'), email_reminder.s('students@gmail', 'reminder to login', '<h1> hello everyone </h1>'), name = 'weekly reminder' )
    #monthly reminder
    sender.add_periodic_task(crontab(hour=14, minute=11, day_of_month='26'), email_reminder.s('students@gmail', 'reminder to login', '<h1> hello everyone </h1>'), name = 'weekly reminder' )


