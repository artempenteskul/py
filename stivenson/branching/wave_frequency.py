wave_frequency = int(input('Enter wave frequency in Hz: '))

wave_category = ''

if wave_frequency < 3 * pow(10, 9):
    wave_category = 'radio'
elif 3 * pow(10, 9) <= wave_frequency < 3 * pow(10, 12):
    wave_category = 'micro'
elif 3 * pow(10, 12) <= wave_frequency < 4.3 * pow(10, 14):
    wave_category = 'infrared'
elif 4.3 * pow(10, 14) <= wave_frequency < 7.5 * pow(10, 14):
    wave_category = 'visible'
elif 7.5 * pow(10, 14) <= wave_frequency < 3 * pow(10, 17):
    wave_category = 'ultraviolet'
elif 3 * pow(10, 17) <= wave_frequency < 3 * pow(10, 19):
    wave_category = 'x-ray'
elif 3 * pow(10, 19) <= wave_frequency:
    wave_category = 'gamma'

print(f'Wave frequency is {wave_frequency}\n'
      f'Wave category is {wave_category}')
