'''
pip install schedule
'''

import schedule
import time

def job():
    print("1 minute")

def jobsec():
    print("1 second")

schedule.every(1).seconds.do(jobsec)
schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
#schedule.every().to().minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)