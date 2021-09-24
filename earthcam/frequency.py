#!/usr/bin/python3.7m
import datetime
import configparser
import _thread as thread
import time
import takephotos

# read config
conf = configparser.ConfigParser()
conf.read('/home/pi/strato3/earthcam/mission_conf.ini')
# this is to ensure a thread is only started once
onlineThreads = []

# this function is executed in every thread
def PhotoThread(Phase, frequency, endTime):
    now = datetime.datetime.now()
    # sleep time is calculated by dividing 1 minute with the photos per minute
    sleepTime = round(60 / frequency)
    # if this loop ends the thread exits
    while (now.timestamp() < endTime.timestamp()):
        print(now)
        print(sleepTime)
        takephotos.capture(now)
        time.sleep(sleepTime)
        now = datetime.datetime.now()

while 1:
    now = datetime.datetime.now()
    for section in conf.sections():
        # convert date into timestamp
        begin = datetime.datetime.strptime(conf.get(section, 'begin'), '%Y-%m-%d %H:%M %z')
        end = datetime.datetime.strptime(conf.get(section, 'end'), '%Y-%m-%d %H:%M %z')
        print(onlineThreads)
        # check if time is between start and end
        if (now.timestamp() >= begin.timestamp() and now.timestamp() < end.timestamp() and (not section in onlineThreads)):
            PhotosPerMinute = int(conf.get(section, 'PhotosPerMinute'))
            try:
                print(section, "will be started")
                thread.start_new_thread( PhotoThread, (section, PhotosPerMinute, end, ) )
                onlineThreads.append(section)
            except:
                print ("Error: unable to start thread")
        else:
            print(section, "not active")
    # perform this only every minute
    time.sleep(60)
