days = int(input('Enter days quantity:\n'))
hours = int(input('Enter hours quantity:\n'))
minutes = int(input('Enter minutes quantity:\n'))
seconds = int(input('Enter seconds quantity:\n'))

amount_of_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds

print(f'Amount of seconds: {amount_of_seconds}')
