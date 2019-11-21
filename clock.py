from apscheduler.schedulers.blocking import BlockingScheduler
import os

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    os.system(
        '''
        curl -n -X DELETE https://api.heroku.com/apps/pic-metric-1/dynos \
        -H "Content-Type: application/json" \
        -H "Accept: application/vnd.heroku+json; version=3"
        '''
        )
    print('It is working..')

sched.start()