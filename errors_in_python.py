def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    return dividend / divisor


students = [
    {'name': 'Bob', 'grades': [75, 90]},
    {'name': 'Rolf', 'grades': []},
    {'name': 'Jen', 'grades': [100, 90]}
]

try:
    for student in students:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades), len(grades))
        print(f'{name} averaged {average}.')
except ZeroDivisionError:
    print(f'ERROR {name} has no grades.')

else:
    print('-- All student average grades are calculated --')
finally:
    print('-- End of student average calculation')




'''
print('Welcome to average grade program.')
try:
    average = divide(sum(grades), len(grades)) # it's starting def divide, than raise error and going to except
except ZeroDivisionError as e: # ZeroDivisionError is already have a text from def divide
    # ZeroDivisionError, RuntimeError, ValueError etc
    print(e)
    print('There are no grades yet in your list')
else:
    print(f'The average grade is {average}')
finally:
    print('Thank you!')

'''
