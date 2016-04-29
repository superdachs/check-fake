#!/usr/bin/env python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#            
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#                            
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# 2016 Stefan Kauerauf
# <mail@stefankauerauf.de>

VERSION = "0.1"

__doc__ = "Nagios fake plugin for testing and demonstration purposes."

modes = ['fixed']

import argparse
import sys
import os
import time

try:
    hostname = os.environ['NAGIOS_HOSTNAME']
    servicename = os.environ['NAGIOS_SERVICEDESC']
except:
    hostname = "test"
    servicename = "test"


argp = argparse.ArgumentParser(description=__doc__)
argp.add_argument('-M', '--mode', help="timer mode (fixed)")
argp.add_argument('-L', '--statuslist', help="list with status like 'wcwocuwwoo' (o = ok, w = warning, c = critical, u = unknown) or 'oduoddouo' (o = up, d = down, u = unreachable) for host checks. If no list is given, status will be random.")
argp.add_argument('-T', '--changetime', help='time to change status in seconds or random (default 1s)')
argp.add_argument('-H', '--hostcheck', default=False, action="store_true", help="simulate host check")
argp.add_argument('-P', '--performancedata', default=False, action="store_true", help="generate fake perf data")
argp.add_argument('-V', '--variable', default='var', help="fake variable name for service check mode")
argp.add_argument('-w', '--warning')
argp.add_argument('-c', '--critical')


args = argp.parse_args()


# checking arguments
if args.mode not in modes:
    print("mode must be in %s" % " ".join(modes))
    sys.exit(3)

if args.hostcheck:
    if args.variable != "var":
        print("variable name only suitable for service checks not host")
        sys.exit(3)

    for elem in args.statuslist:
        if elem not in 'odu':
            print('allowed status for hostchecks only o = up, d = down, u = unreachable')
            sys.exit(3)

else:
    for elem in args.statuslist:
        if elem not in 'owcu':
            print('allowd status for service checks only o = ok, w = warning, c = critical, u = unknown')


try:
    int(args.changetime)
except:
    if args.changetime != 'random':
        print('change time must be a integer number or "random"')


# get the old check time
newtime = int(time.time())

firstrun = False
try:
    with open("/tmp/check_fake_%s_%s" % (hostname, servicename), 'r') as f:
        cnt = f.read().split("|")
        oldtime = int(cnt[0])
        oldindex = int(cnt[1])
except Exception as e:
    print(e)
    oldtime = newtime
    oldindex = 0
    firstrun = True

newindex = oldindex + 1
if newindex == len(args.statuslist):
    newindex = 0


# get the time difference
if args.changetime != 'random':
    diff = int(args.changetime)
else:
    diff = random.randint(3000, 30000)

# change status
if newtime - oldtime > diff or firstrun:
    status = args.statuslist[newindex]
    with open("/tmp/check_fake_%s_%s" % (hostname, servicename), 'w') as f:
        f.write(str(newtime) + "|" + str(newindex))
else:
    status = args.statuslist[oldindex]

service_status = {'o': ['OK', 0], 'w': ['WARNING', 1], 'c': ['CRITICAL', 2], 'u': ['UNKNOWN', 3]}
host_status = {'o': ['UP', 0], 'd': ['DOWN', 1], 'u': ['UNREACHABLE', 2]}

# generate values
if status = 'o':
    value = int(args.warning - 1)
elif status = 'w':
    value = int(args.warning + 1)
elif status = 'c':
    value = int(args.critical + 1)



if args.hostcheck:
    ret = host_status[status][1]
    string = host_status[status][0]
else:
    ret = service_status[status][1]
    string = service_status[status][0]
    string = string + " " + args.variable + " " 



