employee_rating = float(input('Enter the rating of the employee (choices: 0.0; 0.4; 0.6 and more): '))

allowance = 0

if employee_rating == 0:
    allowance = 0
elif employee_rating == 0.4:
    allowance = 0.4 * 2400
elif employee_rating >= 0.6:
    allowance = employee_rating * 2400

print(f'Employee rating is {employee_rating:.2f}\n'
      f'Employee allowance is {allowance}$')
