earthquake_grade = float(input('Enter the grade of the earthquake: '))

earthquake_description = ''

if earthquake_grade < 2:
    earthquake_description = 'minimal'
elif 2 <= earthquake_grade < 3:
    earthquake_description = 'very weak'
elif 3 <= earthquake_grade < 4:
    earthquake_description = 'weak'
elif 4 <= earthquake_grade < 5:
    earthquake_description = 'intermediate'
elif 5 <= earthquake_grade < 6:
    earthquake_description = 'moderate'
elif 6 <= earthquake_grade < 7:
    earthquake_description = 'strong'
elif 7 <= earthquake_grade < 8:
    earthquake_description = 'very strong'
elif 8 <= earthquake_grade < 10:
    earthquake_description = 'great'
elif earthquake_grade >= 10:
    earthquake_description = 'destructive'

print(f'Earthquake grade is {earthquake_grade} ({earthquake_description})')
