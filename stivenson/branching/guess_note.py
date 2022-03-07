note_frequency = float(input('Enter the frequency of the note: '))

if 260 < note_frequency < 262:
    print('It seems to be C4 note')
elif 292 < note_frequency < 295:
    print('It seems to be D4 note')
elif 328 < note_frequency < 330:
    print('It seems to be E4 note')
elif 348 < note_frequency < 350:
    print('It seems to be F4 note')
elif 391 < note_frequency < 393:
    print('It seems to be G4 note')
elif 439 < note_frequency < 441:
    print('It seems to be A4 note')
elif 493 < note_frequency < 495:
    print('It seems to be B4 note')
else:
    print(f'I don\'t know note with {note_frequency} frequency')
