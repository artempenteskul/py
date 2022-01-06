year = int(input('Enter the year: '))

animal = ''

if 2000 % 12 == year % 12:
    animal = 'dragon'
elif 2001 % 12 == year % 12:
    animal = 'snake'
elif 2002 % 12 == year % 12:
    animal = 'horse'
elif 2003 % 12 == year % 12:
    animal = 'goat'
elif 2004 % 12 == year % 12:
    animal = 'monkey'
elif 2005 % 12 == year % 12:
    animal = 'rooster'
elif 2006 % 12 == year % 12:
    animal = 'dog'
elif 2007 % 12 == year % 12:
    animal = 'pig'
elif 2008 % 12 == year % 12:
    animal = 'rat'
elif 2009 % 12 == year % 12:
    animal = 'bull'
elif 2010 % 12 == year % 12:
    animal = 'tiger'
elif 2011 % 12 == year % 12:
    animal = 'rabbit'

if animal:
    print(f'You were born in the year of {animal.upper()}')
else:
    print('You typed something wrong')

