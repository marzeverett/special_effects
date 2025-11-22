# Indivdual Effects Explanations 

## Python - in Special Effects Library

### clock.py
#Almost Direct copy from here: https://keithweaverca.medium.com/controlling-stepper-motors-using-python-with-a-raspberry-pi-b3fbd482f886

RPIO.GPIO - board mode
7, 11, 13, 15 are the control pins
Stepper sequence - rotation of clock hand.

### erratic_flowers.py
#Based on waveshare servo hat example code
PCA9685 Servo Controller Hat 
Runs come crazy pulses 
Servo control address in code is 0x40 for hat 
In the wiring, its hat section 0 
pwm.setServoPulse(section, pulse)

### knock_over.py 
#Based on waveshare servo hat example code
PCA9685 Servo Controller Hat 
Runs an over and back pulse with a wait 
Servo control address in code is 0x40 for hat 
In the wiring, its hat section 8
pwm.setServoPulse(section, pulse)

### shaking_box.py
#Based on waveshare servo hat example code
PCA9685 Servo Controller Hat 
Runs a few mild pulses
Servo control address in code is 0x40 for hat 

In the wiring, its hat section 4
pwm.setServoPulse(section, pulse)

### music_box.py
#Almost Direct copy from here: https://keithweaverca.medium.com/controlling-stepper-motors-using-python-with-a-raspberry-pi-b3fbd482f886

RPIO.GPIO - board mode
29, 31, 33, 35 are the control pins
Stepper sequence - rotation of ballerina thing

### lantern_off.py
Just sends serial number to plugged in arduino - in this case, 4

### lantern_on.py 

Just sends serial number to plugged in arduino - in this case, 5


## Carried out by Arduino 
### Neopixel Ring
HP_Light_Up_Ring.ino 
Neopixels connected on pin 4
12 neopixel ring
Reads from serial:
- If number 8:
    - Show all Yellow
    - Delay
    - Clear
- If number 5:
    - Fill all pixels with yellow
    - DON'T clear
- If number 4:
    - clear all neopixels 

### IR Input
IR_Remote.ino
Receiver on pin 11 
- Decode IR
- Translate it
- Send via serial 
- Default is other button 
- Delay 