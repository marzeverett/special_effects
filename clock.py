


#Almost Direct copy from here: https://keithweaverca.medium.com/controlling-stepper-motors-using-python-with-a-raspberry-pi-b3fbd482f886

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,15,13]
for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
        halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
        ]

def action(message):
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)
    GPIO.cleanup()

action("hi")



# #name associated with device ID and action
# import time
# import RPi.GPIO as GPIO
# from RpiMotorLib import RpiMotorLib

# #clock_pins = [17, 18, 27, 22]
# clock_pins = [7, 11, 15, 13]
# clock_motor = RpiMotorLib.BYJMotor("StepperMotor", "28BYJ")


# sleep_time = 1.5

# def action(message):
#     clock_motor.motor_run(clock_pins, .003, 500, False, False, "wave", .05) #.005 $
#     time.sleep(4)
#     GPIO.cleanup()


# action("hi")