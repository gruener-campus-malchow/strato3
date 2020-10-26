#!/usr/bin/python3.6
import datetime
import configparser
import _thread as thread
import time

conf = configparser.ConfigParser()
conf.read('/home/video/strato3/horizoncam/mission_conf.ini')

def printFrequency(Phase, frequency):
    print(Phase + " " + frequency)

   # time.sleep(1)

while 1:
    now = datetime.datetime.now()
    for section in conf.sections():
        begin = datetime.datetime.strptime(conf.get(section, 'begin'), '%Y-%m-%d %H:%M')
        end = datetime.datetime.strptime(conf.get(section, 'end'), '%Y-%m-%d %H:%M')
        if (now >= begin and now < end):
            PhotosPerMinute = conf.get(section, 'PhotosPerMinute')
            try:
                thread.start_new_thread( printFrequency, (section, PhotosPerMinute,  ) )
            except:
                print ("Error: unable to start thread")
    time.sleep(60)
