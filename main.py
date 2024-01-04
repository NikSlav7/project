from gpiozero import DistanceSensor, OutputDevice
from time import sleep, time

# Initialize ultrasonic sensors for the doorway entrance and exit
entrance_sensor = DistanceSensor(echo=27, trigger=17)
exit_sensor = DistanceSensor(echo=23, trigger=22)

# Initialize relay module control pin on GPIO 18
relay = OutputDevice(18)

# Set initial state of the relay (off)
relay.off()

# Initialize a variable to track the number of people in the room
people_in_room_count = 0

# Initialize variables to track the last entrance and exit times
last_entrance_time = 0
last_exit_time = 0

# Define the delay duration (in seconds) to avoid re-triggering the sensors
delay_duration = 3

try:
    while True:
        # Wait for the sensors to settle
        sleep(0.1)

        # Measure distances in centimeters from both sensors
        entrance_distance_cm = entrance_sensor.distance * 100
        exit_distance_cm = exit_sensor.distance * 100

        # Check if someone is passing through the entrance (e.g., within 50 cm)
        if entrance_distance_cm < 50 and time() - last_exit_time > delay_duration:
            print("Someone entered the room!")

            # Increase the count of people in the room
            people_in_room_count += 1

            # Update the last entrance time
            last_entrance_time = time()

            # If it's the first person entering, turn on the light
            if people_in_room_count == 1:
                relay.on()
                print("Light turned on.")

        # Check if someone is passing through the exit (e.g., within 50 cm)
        elif exit_distance_cm < 50 and time() - last_entrance_time > delay_duration:
            print("Someone exited the room!")

            # Update the last exit time
            last_exit_time = time()

            # Decrease the count of people in the room
            if people_in_room_count > 0:
                people_in_room_count -= 1

                # If everyone has left the room, turn off the light
                if people_in_room_count == 0:
                    relay.off()
                    print("Light turned off.")

        # Wait for a short period before reading again
        sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    # Ensure the relay is off when exiting
    relay.off()
