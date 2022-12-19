

#name associated with device ID and action
import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

clock_pins = [17, 18, 27, 22]
clock_pins = [7, 11, 13, 15]
clock_motor = RpiMotorLib.BYJMotor("StepperMotor", "28BYJ")


sleep_time = 1.5

def action(message):
    clock_motor.motor_run(clock_pins, .003, 500, False, False, "wave", .05) #.005 $
    time.sleep(4)
    GPIO.cleanup()


action("hi")