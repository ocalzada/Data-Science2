from apscheduler.schedulers.blocking import BlockingScheduler
import os

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    os.system('heroku ps:restart')
    print('It is working..')

sched.start()