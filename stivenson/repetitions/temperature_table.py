temperature_table = {k: k * 1.8 + 32 for k in range(101) if k % 10 == 0}

for k in temperature_table:
    print(f'{k} in Celsius is equal to {temperature_table[k]} in Fahrenheit')
