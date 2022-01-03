# PV = nRT

gas_const = 8.314

pressure = float(input('Enter the pressure in the Pascals:\n'))
volume = float(input('Enter the volume in Litres:\n'))
temperature_in_celsius = float(input('Enter the temperature in Celsius:\n'))

temperature_in_kelvins = temperature_in_celsius + 273.15

substance_moles = (pressure * volume) / (gas_const * temperature_in_kelvins)

print(f'The quantity of substance is: {substance_moles:.1f} moles')
