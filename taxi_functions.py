import time


def current_time():
    return time.time()


def kilometer_calculation(start_time,
                          distance_km, status):
    time_difference = current_time() - start_time
    if (time_difference >= 60 and status != 'wait'):
        distance_km = distance_km + 1
        start_time = current_time()
    return distance_km, start_time


def meter_calulation(meter_timer, distance_mtr):
    if (current_time() - meter_timer > 2):
        distance_mtr = distance_mtr + 200
        meter_timer = current_time()
    return distance_mtr, meter_timer


def increase_speed(speed):
    speed = speed + 5
    print('Speed increased by 5,\
           current speed =', speed)
    return speed


def decrease_speed(speed):
    speed = speed - 5
    print('Speed decreased by 5,\
           current speed = ', speed)
    return speed


def wait_period(wait_fee):
    wait_start = current_time()
    print("Taxi in wait state. \
          Press ctrl+c and R to end wait")
    try:
        while True:
            if (current_time() - wait_start > 60):
                wait_fee = wait_fee + 1
                wait_start = current_time()
    except KeyboardInterrupt:
        pass
    return wait_fee


def fare_calculation(distance_km, wait_fee):
    fare_per_km = 3
    fare = distance_km * fare_per_km
    fare = fare + wait_fee
    return fare


def average_speed(distance, time):
    return round(distance/time)


def output(total_time, distance_km,
           avg_speed, wait_fee,
           total_fare):
    print("Ride time: ", total_time,
          " Seconds")
    print("Distance: ", distance_km,
          " KM")
    print("Avg. speed: ", avg_speed,
          " Meters per second")
    print("Wait time: ", wait_fee,
          " Minutes")
    print("Fare: $", total_fare)


