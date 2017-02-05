#!/usr/bin/env python

import argparse
import time

import Adafruit_MCP3008

# Software SPI configuration
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25


def main(args):
  mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
  while True:
      print 'Light reading=%d' % mcp.read_adc(args.channel)
      time.sleep(0.5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='GreenPiThumb Light Sensor Diagnostic Test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-c',
        '--channel',
        type=int,
        help='ADC channel that light sensor is plugged in to',
        default=0)
    main(parser.parse_args())
