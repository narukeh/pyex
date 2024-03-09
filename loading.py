#!/usr/bin/env python3
import time

ct=1
while (ct < 10):
    print('\r-', end='')
    time.sleep(0.1)
    print('\r/', end='')
    time.sleep(0.1)
    print('\r|', end='')
    time.sleep(0.1)
    print('\r\\', end='')
    ct += 1
print()
