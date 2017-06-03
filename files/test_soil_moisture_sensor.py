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
    GPIO.setup(args.gpio_pin, GPIO.OUT)

    mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

    try:
        while True:
            GPIO.output(args.gpio_pin, GPIO.HIGH)
            reading = mcp.read_adc(args.channel)
            print 'Soil mositure level: %d' % reading
            GPIO.output(args.gpio_pin, GPIO.LOW)
            time.sleep(0.5)
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='GreenPiThumb Soil Moisture Diagnostic Test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--gpio_pin',
        type=int,
        help='Pin to power moisture sensor',
        default=16)
    parser.add_argument(
        '-c',
        '--channel',
        type=int,
        help='ADC channel that moisture sensor is plugged in to',
        default=7)
    main(parser.parse_args())
