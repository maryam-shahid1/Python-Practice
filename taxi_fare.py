from taxi_functions import *


def main():

    distance_km = 0
    distance_mtr = 0
    speed = 0
    status = ''
    wait_fee = 0
    kilometer_timer = meter_timer = ride_start = current_time()

    while (True):

        distance_km, kilometer_timer = kilometer_calculation(
            kilometer_timer, distance_km, status)

        distance_mtr, meter_timer = meter_calulation(
            meter_timer, distance_mtr)

        key = input("enter key: ")

        if key == 'W':
            speed = increase_speed(speed)
        if key == 'S':
            speed = decrease_speed(speed)
        if key == 'P' or key == 'p':
            status = 'wait'
            wait_fee = wait_period(wait_fee)
        if key == 'R' or key == 'r':
            status = 'driving'
        if key == 'E' or key == 'e':
            ride_end = current_time()
            break

    total_fare = fare_calculation(distance_km, wait_fee)
    total_time = round(ride_end-ride_start)
    avg_speed = average_speed(distance_mtr, total_time)
    output(total_time, distance_km, avg_speed, 
           wait_fee, total_fare)


if __name__ == "__main__":
    main()


