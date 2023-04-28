# The distance sensor requires you to use the actual pin names instead of the
# explorer hat pin names
# If you look at any examples online it will say to use a voltage divider, but
# it is not needed if you use the explorer hat since the inputs are 5V safe.
# If you are using with guizero you can set up a repeat timer

import explorerhat as eh
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # prevents warnings from appearing

TRIG = 2    #set the pin for the trigger signal, it uses the SDA connector
ECHO = 23   #this is the signal pin, it is input 1 on the eh

GPIO.setup(TRIG,GPIO.OUT)   # set up the pins
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)     # set the trigger to false(off)
print("distance started")
starttime = time.time()     # give initial values to start and stop
stoptime = time.time()      # this prevents an error if the first start time is missed

def distance():
    #print("distance started")
    eh.SDA.on()  # give the trigger a small pulse to send out the sound wave
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    
    while GPIO.input(ECHO) == 0:    # saves start time
        starttime = time.time()
        
    while GPIO.input(ECHO) == 1:    # saves the time of arrival
        stoptime = time.time()
        
    timeelapsed = stoptime - starttime 
    distance = (34300 * timeelapsed)/2  # distance = speed x time
    if distance < 200:      #only outputs distances less than 200cm(you can change)
        print(distance, "cm")
 
while True:
    distance()
    time.sleep(1)
    
