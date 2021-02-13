# Simple Python

# print(divmod(9, 4))
#
# print(int(98.4))

# start = 'na' * 4 + '\n'
# middle = 'hey' * 3 + '\n'
# end = 'goodbye'

# print(start + start + middle + end)

# First
seconds_per_hour = 60 * 60
print(seconds_per_hour)
seconds_per_day = seconds_per_hour * 24
print(seconds_per_day)
print(seconds_per_day / seconds_per_hour)
print(seconds_per_day // seconds_per_hour)

# Second

years_list = [2002, 2003, 2004, 2005, 2006, 2007]
print(years_list[3])
five = years_list[5]

things = ['mozarella', 'cinderella', 'salmonella']
things[2] = 'Cinderella'
print(things)
things[1] = things[1].upper()
print(things)
del things[2]
print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
surprise[2] = surprise[2].lower()

e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

f2e = list(e2f.items())
print(f2e)

print(e2f.keys())

# Third
guess_me = 7

if guess_me > 7:
    print('too more')
elif guess_me < 7:
    print('too low')
else:
    print('its 7')

start = 1

while guess_me > start:
    print('too low')
    start += 1
    if guess_me == start:
        print('found it')
        break

arrs = [3, 2, 1, 0]

for arr in arrs:
    print(arr)

a = [num for num in range(10) if num % 2 == 0]
print(a)

a = list(range(10))

# gg
squares = {key: key * key for key in range(10)}
print(squares)

odd = {num for num in range(10) if num % 2 == 1}
print(odd)

# gg
for thing in ('got %s' % num for num in range(10)):
    print(thing)


def good():
    return ['Harry', 'Ron', 'Hermione']


def get_odds():
    for num in (1, 10, 2):
        yield num


for count, num in enumerate(get_odds(), 1):
    if count == 3:
        print('The third odd num is', num)
        break
