C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

note = input('Enter the note (for example C4): ')

note_name, note_octave = note[0], int(note[1])
note_frequency = 0

if note_name.lower() == 'c':
    note_frequency = C4_FREQ
elif note_name.lower() == 'd':
    note_frequency = D4_FREQ
elif note_name.lower() == 'e':
    note_frequency = E4_FREQ
elif note_name.lower() == 'f':
    note_frequency = F4_FREQ
elif note_name.lower() == 'g':
    note_frequency = G4_FREQ
elif note_name.lower() == 'a':
    note_frequency = A4_FREQ
elif note_name.lower() == 'b':
    note_frequency = B4_FREQ

note_frequency = note_frequency / pow(2, 4 - note_octave)

if note_frequency == 0:
    print('You entered wrong note. Try again!')
else:
    print(f'{note} note has frequency: {note_frequency:.2f}')
