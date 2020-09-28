#!/usr/bin/python3
import datetime
import configparser

conf = configparser.ConfigParser()
conf.read('/home/video/Schreibtisch/mission_conf.ini')


def getfrequency():
    now = datetime.datetime.now()
    for section in conf.sections():
        print(section)
        if (now > datetime.datetime.strptime(conf.get(section, 'begin'), '%Y-%m-%d %H:%M')):
            print(True)
        else:
            print(False)


getfrequency()
