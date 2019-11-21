from apscheduler.schedulers.blocking import BlockingScheduler
import os

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    os.system(
        '''
        curl -n -X DELETE https://api.heroku.com/apps/pic-metric-1/dynos \
        -H "Authorization: Bearer b6c95ae1-b7bb-4d7f-b8dd-26160046655b" \
        -H "Accept: application/vnd.heroku+json; version=3" \
        -H "Content-Type: application/json"
        '''
        )
    print('It is working..')

sched.start()