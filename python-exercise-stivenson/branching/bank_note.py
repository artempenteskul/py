bank_note = int(input('Enter the denomination of the bank note to know who is displayed on it: '))

person = ''

if bank_note == 1:
    person = 'George Washington'
elif bank_note == 2:
    person = 'Thomas Jefferson'
elif bank_note == 5:
    person = 'Abraham Lincoln'
elif bank_note == 10:
    person = 'Alexander Hamilton'
elif bank_note == 20:
    person = 'Andrew Jackson'
elif bank_note == 50:
    person = 'Ulysess Grant'
elif bank_note == 100:
    person = 'Benjamin Franklin'


if person:
    print(f'{person} is displayed on the {bank_note}$ bank note ')
else:
    print('You entered wrong bank note denomination. Try again')
