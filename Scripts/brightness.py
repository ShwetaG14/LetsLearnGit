#!/usr/bin/env python

import sys
import os



def set_brightness(perc):
    os.chdir('/sys/class/backlight/intel_backlight/')
    f = open('brightness', 'w')
    max_bright = 937
    new_brightness =  int((float(perc) / 100)  * max_bright); print(new_brightness)
    f.write(str(new_brightness))
    f.close()

if __name__ == '__main__':
    set_brightness(sys.argv[1])

