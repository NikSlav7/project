import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#relay.off()
people = 0

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance

try:
    while True:
        sleep(0.1)
        
        # distants uksest (cm)
        distance = distance()

        if distance < 50:
            sleep(1)
            new_distance = distance()
            
            if distance > new_distance:
                print("entered")
                people += 1
                
                if people == 1:
                    #relay.on()
                    print("Light on")
        
        else:
            if distance < new_distance:
                print("exited")
                people -= 1
                
                if people == 0:
                    #relay.off()
                    print("Light off")
            
        sleep(1)

except KeyboardInterrupt:
    print("stop")
    #relay.off()
