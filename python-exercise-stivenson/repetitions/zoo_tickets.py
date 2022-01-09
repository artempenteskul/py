age = input('Enter the age of the first person: ')

total = 0

while age != '':
    person_age = int(age)

    if person_age <= 2:
        total += 0
    elif 3 <= person_age <= 12:
        total += 14
    elif person_age >= 65:
        total += 18
    else:
        total += 23

    age = input('Enter the age of the first person: ')

print(f'Total cost for all tickets is: {total:.2f}$')
