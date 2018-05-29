#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:42:38 2017

@author: dieter
"""

import board.Maestro as Maestro
import sys
import glob
import serial
import time
import gc
from scipy.interpolate import interp1d
import itertools

def serial_ports(try_ports=False):
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    if not try_ports: return ports
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def normalize(value, min_value, max_value):
    """Normalizes value to the interval [0,1]
    
    :param value: Value to be normalized 
    :type value: Float
    :param min_value: Value to be mapped to 0
    :type min_value: Float
    :param max_value: Value to be mapped to 1
    :type max_value: Float
    :return: Normalized value
    """
    delta = max_value - min_value
    new = value - min_value
    new = new / delta
    if new < 0: new = 0
    if new > 1: new = 1
    return new


def delete_instances(type_string, skip_ids=[], verbose=False):
    for obj in gc.get_objects():
        if type_string in str(type(obj)):
            identifier = obj.id
            if identifier not in skip_ids:
                obj.__del__(True)
                if verbose: print('Deleted:', str(obj), 'id:', identifier)


#'Board.Board'
#self.id

def connect(verbose=False, try_ports=False):
    ports = serial_ports(try_ports=try_ports)
    ports.sort()
    if verbose: print('Ports Found: ' + str(ports),)
    for port in ports:
        if verbose: print('++ Trying port', port)
        delete_instances('Board.Board', verbose=False)
        b = Board(con_port=False, ser_port=port, verbose=False)
        try:
            b.get_photo()
            b.get_pot()
            b.set_led1(True)
            b.set_led2(True)
            time.sleep(0.25)
            b.set_led1(False)
            b.set_led2(False)

            if verbose: print('++++ Success on port', port)
            break

        except IndexError:
            if verbose: print('++++ Rejected port', port)
        except TypeError:
            if verbose: print('++++ Rejected port', port)
    return b


class Board:
    """Class handling communication with the board.

    :param con_port: Command Port to use
    :type con_port: Str
    :param ser_port: TLL Port to use
    :type ser_port: Str
    """
    def __init__(self, con_port=None, ser_port=None, verbose=False):
        self.id = id(self)
        self.verbose = verbose
        
        if self.verbose: print('Board instance ' + str(self.id) + ' created')
        delete_instances('Board.Board', skip_ids=[self.id], verbose=verbose)

        self.device = Maestro.Device(con_port, ser_port)
        self.servo1 = 0
        self.servo2 = 1
        self.led1 = 2
        self.led2 = 3
        self.pot = 4
        self.photo = 5

        self.photo_min = 30
        self.photo_max = 210

        self.pot_min = 0.25
        self.pot_max = 234

        self.min_servo = 544
        self.zero_servo = 1500
        self.max_servo = 2400
        self.offset_servo = -150

    def __del__(self, msg=False):
        if msg and self.verbose: print('Board instance ' + str(self.id) + ' deleted:')
        try:
            self.stop_all()
            if msg and self.verbose: print('--> ' + str(self.id) + ' Stopped')
        except:
            pass
        try:
            self.device.__del__()
            if msg and self.verbose: print('--> ' + str(self.id) + ' Device Deleted')
        except:
            pass

    def get_photo(self):
        """ Gets the normalized level of the photocell.
        
        :return: float
            Level of the photocell in the range [0, 1].
        """
        photo = self.device.get_position(self.photo)
        photo = normalize(photo, self.photo_min, self.photo_max)
        return photo

    def get_pot(self):
        """Get the normalized level of the potentiometer.
        
        :return: float
            Level of the potentiometer in the range [0, 1].
        """
        pot = self.device.get_position(self.pot)
        pot = 1 - normalize(pot, self.pot_min, self.pot_max)
        return pot

    def set_servo(self, nr, target, raw):
        new = raw
        if not raw:
            f = interp1d([0,0.5,1], [self.min_servo, self.zero_servo + self.offset_servo, self.max_servo])
            new = f(target)
            
        self.device.set_target(nr, int(new))

    def set_led(self, nr, value):
        if value: new = self.max_servo
        if not value: new = self.min_servo
        result = self.device.set_target(nr, new)
        return result

    def set_leds(self, l1, l2):
        """Shortcut to set both LEDs at the same time.
        
        :param l1: State of LED 1
        :type l1: Bool
        :param l2: State of LED 2
        :type l2: Bool
        :return: None
        """
        result1 = self.set_led1(l1)
        result2 = self.set_led2(l2)
        return result1, result2

    def set_servo1(self, position, raw=False):
        """ Set the position of servo 1.
        
        :param position: Normalized target position [0, 1] for the servo.
        :type position: Float
        :param raw: If true, position is given in steps.
        :type raw: Bool
        :return: None
        """
        self.set_servo(self.servo1, position, raw)

    def set_servo2(self, target, raw=False):
        """ Set the position of servo 2.
        """
        self.set_servo(self.servo2, target, raw)

    def set_led1(self, value):
        """Set state of LED 1.
        
        :param value: State of LED 1.
        :type value: Bool
        :return: None
        """
        result = self.set_led(self.led1, value)
        return result

    def set_led2(self, value):
        """Set state of LED 2."""
        result = self.set_led(self.led2, value)
        return result

    def stop_all(self):
        """Set all motors to a neutral position and switch of both LEDs.
        
        :return: None
        """
        self.set_servo1(0.5)
        self.set_servo2(0.5)
        self.set_led1(False)
        self.set_led2(False)


    def calibrate_channel(self, channel, n=10):
        mx = 0
        mn = 1000
        for x in range(0, n):
            time.sleep(1)
            print('.', end='')
            value = self.device.get_position(channel)
            if value > mx: mx = value
            if value < mn: mn = value
        print()
        return mn, mx

    def calibrate_photo(self):
        """ Function to calibrate the photocell. A number of measurements will be taken. The recorded minimum and 
        maximum values are used to normalize subsequent measurements.
        
        :return: Minimum and maximum value.
        """
        print('Calibrating photocell', end='')
        mn, mx = self.calibrate_channel(self.photo, 5)
        self.photo_min = mn
        self.photo_max = mx
        return mn, mx

    def calibrate_pot(self):
        """ Function to calibrate the potentiometer. A number of measurements will be taken. The recorded minimum and 
        maximum values are used to normalize subsequent measurements.

        :return: Minimum and maximum value.
        """
        print('Calibrating pot', end='')
        mn, mx = self.calibrate_channel(self.pot, 10)
        self.pot_min = mn
        self.pot_max = mx
        return mn, mx


if __name__ == '__main__':
    print(serial_ports())
