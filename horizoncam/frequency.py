#!/usr/bin/python3.7m
import datetime
import configparser
import _thread as thread
import time
import takephotos

conf = configparser.ConfigParser()
conf.read('/home/pi/strato3/horizoncam/mission_conf.ini')
onlineThreads = []

def PhotoThread(Phase, frequency, endTime):
    #print(Phase + " " + frequency)
    now = datetime.datetime.now()
    sleepTime = round(60 / frequency)
    while (now.timestamp() < endTime.timestamp()):
        print(now)
        print(sleepTime)
        takephotos.capture(now)
        time.sleep(sleepTime)
        now = datetime.datetime.now()

while 1:
    now = datetime.datetime.now()
    for section in conf.sections():
        begin = datetime.datetime.strptime(conf.get(section, 'begin'), '%Y-%m-%d %H:%M %z')
        end = datetime.datetime.strptime(conf.get(section, 'end'), '%Y-%m-%d %H:%M %z')
        print(onlineThreads)
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
    time.sleep(60)
