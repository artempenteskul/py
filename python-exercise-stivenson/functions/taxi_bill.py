from math import ceil

taxi_distance = float(input('Enter distance of the drive in kilometres: '))

BASIC_BILL = 4
COST_PER_140_METRES = 0.25


def taxi_bill(distance):
    distance_in_metres = distance * 1000
    times_140_metres = ceil(distance_in_metres / 140)
    return BASIC_BILL + times_140_metres * COST_PER_140_METRES


print(f'Taxi distance - {taxi_distance} km\n'
      f'Price - {taxi_bill(taxi_distance)} $')
