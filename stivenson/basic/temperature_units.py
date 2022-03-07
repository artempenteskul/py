from fractions import Fraction


temperature_in_celsius = float(input('Enter the temperature in Celsius:\n'))

temperature_in_fahrenheit = (temperature_in_celsius * Fraction(9, 5) + 32)
temperature_in_kelvins = temperature_in_celsius + 273.15

print(f'Temperature in Celsius: {temperature_in_celsius:.2f}\n'
      f'Temperature in Fahrenheits: {temperature_in_fahrenheit:.2f}\n'
      f'Temperature in Kelvins: {temperature_in_kelvins:.2f}\n')
