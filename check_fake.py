#/usr/bin/env python

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

VERSION = 0.1

__doc__ = "Nagios fake plugin for testing and demonstration purposes."

import argparse





argp = argparse.ArgumentParser(description=__doc__)
argp.add_argument('-M', '--mode', help="timer mode (fixed, random)")
argp.add_argument('-L', '--statuslist', help="list with status like 'wcwocuwwoo' (o = ok, w = warning, c = critical, u = unknown) 
        or 'oduoddouo' (o = up, d = down, u = unreachable) for host checks. If no list is given, status will be random.")
argp.add_argument('-H', '--hostcheck', default=False, action="store_true", help="simulate host check")
argp.add_argument('-P', '--performancedata', default=False, action="store_true", help="generate fake perf data")
argp.add_argument('-V', '--variable', help="")
        
