#!/usr/bin/env python

import argparse

import Adafruit_DHT


def main(args):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,
                                                    args.dht_pin)
    if humidity is not None and temperature is not None:
        print(
            'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='GreenPiThumb DHT11 Diagnostic Test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-p',
        '--dht_pin',
        type=int,
        help='GPIO pin that DHT is plugged in to',
        default=21)
    main(parser.parse_args())
