#from gpiozero import DistanceSensor, OutputDevice
#from time import sleep, time

#sensor = DistanceSensor(echo=22, trigger=4)
#relay = OutputDevice(18)
#relay.off()
people = 0

while True:
    distance = input("Algus: ")
    new_distance = input("Lõpp: ")
            
    if int(distance) > int(new_distance):
        print("entered")
        people += 1
                
        if people >= 1:
            print("Light on")
        
    else:
        if int(distance) < int(new_distance):
            print("exited")
            people -= 1
                
            if people == 0:
                print("Light off")
                
    print("people: " + str(people))
