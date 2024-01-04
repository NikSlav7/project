from gpiozero import DistanceSensor, OutputDevice
from time import sleep

# Initialize ultrasonic sensor with TRIG as GPIO 17 and ECHO as GPIO 27
sensor = DistanceSensor(echo=27, trigger=17)

# Initialize relay module control pin on GPIO 18
relay = OutputDevice(18)

# Set initial state of the relay (off)
relay.off()

# Initialize a variable to track the number of people in the room
people_in_room = 0

try:
    while True:
        # Wait for the sensor to settle
        sleep(0.1)

        # Measure distance in centimeters
        distance_cm = sensor.distance * 100

        # Check if someone is close (e.g., within 50 cm)
        if distance_cm < 50:
            print("Someone entered the room!")

            # Increase the count of people in the room
            people_in_room += 1

            # If it's the first person entering, turn on the light
            if people_in_room == 1:
                relay.on()
                print("Light turned on.")

        else:
            # If someone left the room (distance exceeds 50 cm), decrease the count
            if people_in_room > 0:
                people_in_room -= 1

                # If everyone has left the room, turn off the light
                if people_in_room == 0:
                    relay.off()
                    print("Light turned off.")

        # Wait for a short period before reading again
        sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    # Ensure the relay is off when exiting
    relay.off()
