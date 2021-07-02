# Omni
The next generation of affordable prosthetic arms.

**Connection Guide**
1. Stack Adafruit PWM Servo Hat on Raspberry Pi 3B+ after soldering on headers. 
2. Connect the servos to ports 0 through 4 on the Adafruit Servo hat.
3. Connect separate battery sources (6V for Servo hat) to both the Raspberry Pi and the PWM Servo hat.
4. For the EMG module, connect the Myoware sensor SIG pin to port A3 on the Adafruit Bluefruit Sense Microcontroller.
5. Download Arduino code to microcontroller, and Python code to Raspberry Pi.
6. Connect a microphone/headset system for voice control mode.
