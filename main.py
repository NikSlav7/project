from gpiozero import DistanceSensor, OutputDevice
from time import sleep, time

sensor = DistanceSensor(echo=22, trigger=4)
relay = OutputDevice(18)
relay.off()
people = 0

try:
    while True:
        sleep(0.1)
        
        # distants uksest (cm)
        distance = sensor.distance * 100

        if distance < 50:
            sleep(1)
            new_distance = sensor.distance * 100
            
            if distance > new_distance:
                print("entered")
                people += 1
                
                if people == 1:
                    relay.on()
                    print("Light on")
        
        else:
            if distance < new_distance:
                print("exited")
                people -= 1
                
                if people == 0:
                    relay.off()
                    print("Light off")
            
        sleep(1)

except KeyboardInterrupt:
    print("stop")
    relay.off()
