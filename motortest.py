#Test program to drive the motors
import pcduino
#import time

speed_pin_1 = 'gpio9'
pin_forback = 'gpio11'
pin_go = 'gpio8'

def loop():
	while True:
		gpio.digitalWrite(speed_pin_1, 200)
		gpio.digitalWrite(pin_forback, gpio.HIGH)
		gpio.digitalWrite(pin_go, gpio.HIGH)
