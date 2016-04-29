#!/usr/bin/env python

import argparse
import json
import sys
import os
import time

try:
    hostname = os.environ['NAGIOS_HOSTNAME']
    servicename = os.environ['NAGIOS_SERVICEDESC']
except:
    hostname = "test"
    servicename = "test"

argp = argparse.ArgumentParser()
argp.add_argument("-H", "--host", help="Hostaddress")
argp.add_argument("-C", "--conf", help="Configfile")
argp.add_argument("-P", "--ping", default=False, action="store_true", help="Hostcheck")
argp.add_argument("-S", "--service", help="Name of the service to check")
argp.add_argument("-L", "--list", help="status list ('UP,DOWN,RANDOM,UNREACHABLE')")
argp.add_argument("-T", "--time", help="change time in minutes or RANDOM (1 to 15min) or EVERYTIME")

args = argp.parse_args()

# check the config file
content = ""
try:
    with open(args.conf, 'r') as cf:
        c = cf.read()
        content = json.loads(c)
except Exception as e:
    print(e)


host = None
for elem in content:
    if args.host == elem['hostaddress']:
        host = elem
        break
if not host:
    print("This host is not defined")
    sys.exit(3)

checktime = int(time.time())
firstrun = False

# first check if it is hostcheck
if args.ping:

    # get old check
    try:
        with open("/tmp/check_fake_%s_%s" % (hostname, servicename), 'r') as f:
            cnt = f.read().split('|')
            oldtime = cnt[0]
            oldindex = cnt[1]
    except Exception:
        oldtime = checktime
        oldindex = 0
        firstrun = True

    # get the new status index
    if args.time == "EVERYTIME":
        newindex = oldindex + 1
        if newindex == len(args.list.split(',')):
            newindex = 0
    elif args.time != "EVERYTIME" and args.time != "RANDOM":
        count = newtime - oldtime
        count = count / (int(args.time) * 60)
        count = int(count)
        newindex = oldindex + count
         

    

    
