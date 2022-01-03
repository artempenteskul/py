# q = m * C * (T1 - T2)

water_quantity = int(input('Enter water quantity in grams:\n'))
temperature_difference = float(input('Enter the difference between current temperature and the temperature you want:\n'))

q = water_quantity * 4.186 * temperature_difference

print(f'The amount of energy you need is: {q:.2f} Joules')
