# Simple Python

# print(divmod(9, 4))
#
# print(int(98.4))

# start = 'na' * 4 + '\n'
# middle = 'hey' * 3 + '\n'
# end = 'goodbye'

#print(start + start + middle + end)

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


