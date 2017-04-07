#!/usr/bin/env python

import argparse
import time

import Adafruit_MCP3008
import RPi.GPIO as GPIO

CLK  = 18
MISO = 23
MOSI = 24
CS   = 25


def main(args):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([args.pump_pin1, args.pump_pin2], GPIO.OUT)

    mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

    i = 0
    try:
    while True:
        if i % 2 == 0:
            GPIO.output(args.pump_pin1, GPIO.LOW)
            GPIO.output(args.pump_pin2, GPIO.HIGH)
        else:
            GPIO.output(args.pump_pin1, GPIO.HIGH)
            GPIO.output(args.pump_pin2, GPIO.LOW)
        reading = mcp.read_adc(args.channel)
        if i % 2 == 1:
            reading = 1023 - reading
        print 'Soil mositure level: %d' % reading
        GPIO.output([args.pump_pin1, args.pump_pin2], GPIO.LOW)
        time.sleep(0.5)
        i += 1
    finally:
        GPIO.cleanup()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='GreenPiThumb Soil Moisture Diagnostic Test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--pump_pin1',
        type=int,
        help='Second GPIO pin reading soil moisture',
        default=16)
    parser.add_argument(
        '--pump_pin2',
        type=int,
        help='Second GPIO pin reading soil moisture',
        default=12)
    parser.add_argument(
        '-c',
        '--channel',
        type=int,
        help='ADC channel that moisture sensor is plugged in to',
        default=7)
    main(parser.parse_args())
