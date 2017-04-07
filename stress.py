#!/usr/bin/env python3

import time
import datetime
import sys
from serialClient.serialClient import SerialClient

dev = '/dev/ttyUSB0'
s = SerialClient(dev)
success = 0
total = 0
packet = 123456
interval = 5
while True:
    total += 1
    sys.stdout.write('Sending packet #%s ' % (total))
    begin = time.time()
    resp = s.write('radio tx 123456')[0].strip()
    elapsed = time.time() - begin
    if resp == b'ok':
        sys.stdout.write('successfully ')
        success += 1
    else:
        sys.stdout.write('failed ')
    print('in %s seconds, fail rate = %s/%s (%s %%)' % (elapsed, (total-success), total, (total-success)/total*100))
    sys.stdout.flush()
    #print('=> Sleep %s seconds' % interval)
    time.sleep(interval)

