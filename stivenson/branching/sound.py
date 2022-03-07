level_of_sound = int(input('Enter the level of the sound: '))


if level_of_sound < 40:
    print('Too low level of the sound')
elif level_of_sound == 40:
    print('It seems to be quiet room')
elif 40 < level_of_sound < 70:
    print('It\'s something between quiet room and alarm clock')
elif level_of_sound == 70:
    print('It seems to be alarm clock')
elif 70 < level_of_sound < 106:
    print('It\'s something between alarm clock and gas lawn mower')
elif level_of_sound == 106:
    print('It seems to be gas lawn mower')
elif 106 < level_of_sound < 140:
    print('It\'s something between gas lawn mower and jackhammer')
elif level_of_sound == 140:
    print('It seems to be jackhammer')
elif level_of_sound > 140:
    print('Too high level of sound!')
