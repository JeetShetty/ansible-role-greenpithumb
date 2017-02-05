#!/usr/bin/env python

import argparse
import time

import RPi.GPIO as GPIO


def main(args):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(args.pump_pin, GPIO.OUT)

    try:
        while True:
            print 'turning on pin %d' % args.pump_pin
            GPIO.output(args.pump_pin, GPIO.HIGH)
            time.sleep(3.0)
            print 'turning off pin %d' % args.pump_pin
            GPIO.output(args.pump_pin, GPIO.LOW)
            time.sleep(3.0)
    finally:
      GPIO.cleanup()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='GreenPiThumb Water Pump Diagnostic Test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-p',
        '--pump_pin',
        type=int,
        help='GPIO pin that controls the pump',
        default=26)
    main(parser.parse_args())
