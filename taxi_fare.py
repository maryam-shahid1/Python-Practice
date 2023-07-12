import time

start = time.time()
start_time = time.time()
meter_timer = time.time()
distance_km = 0
distance_meter = 0
wait_start = 0
fare_per_km = 3
status = ''
total_wait = 0
wait_fee = 0
speed = 0
fare = 0

while (True):

    # Assuming one km is covered in a minute
    diff = time.time() - start_time
    if diff >= 60 and status != 'wait':
        distance_km = distance_km + 1
        start_time = time.time()
    
    # Assuming 200 meters are covered in 2 seconds
    if time.time() - meter_timer > 2:
        distance_meter = distance_meter + 200
        meter_timer = time.time()
        
    key = input("enter key: ")

    # Increase speed by 5
    if key == 'W':
        speed = speed + 5
        print('Speed increased by 5, current speed =', speed)
    
    # Decrease speed by 5
    if key == 'S':
        speed = speed - 5
        print('Speed decreased by 5, current speed = ', speed)

    # Change status and start timer for wait period
    if key == 'P' or key == 'p':
        status = 'wait'
        wait_start = time.time()
        print("Taxi in wait state. Press ctrl+c and R to end wait")
        try: 
            while True:
                if time.time() - wait_start > 60:
                    wait_fee = wait_fee + 1
                    wait_start = time.time()
                    total_wait = total_wait + 1
        except KeyboardInterrupt:
            pass

    # Change status and reset timer for wait period
    if key == 'R' or key == 'r':
        status = 'driving'
        wait_start = 0
    
    # End taxi ride
    if key == 'E' or key == 'e':
        end = time.time()
        break


fare = distance_km * fare_per_km
total_fare = fare + wait_fee
total_time = round(end-start)
avg_speed = round(distance_meter/total_time)

print("Ride time: ", total_time, " Seconds")
print("Distance: ", distance_km, " KM")
print("Avg. speed: ", avg_speed, " Meters per second")
print("Wait time: ", total_wait, " Minutes")
print("Fare: $", total_fare)
