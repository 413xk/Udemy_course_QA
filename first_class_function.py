def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    print(dividend / divisor)
    return dividend / divisor


def calculate(*values, operator):
    print(operator(*values))
    return operator(*values)


result = calculate(20, 2, operator=divide)

print(result)


# EXAMPLE 2


def search(sequence, expected, finder):
    for elem in sequence: # elem = each dict in 'friends'
        if finder(elem) == expected: # finder = get_friend_name(friend)
            return elem
    raise RuntimeError(f'Could not find an element with {expected}')


friends = [
    {'name': 'Rolf Smith', 'age': 24},
    {'name': 'Adam Wool', 'age': 30},
    {'name': 'Anne Pun', 'age': 27},
]


def get_friend_name(friend):
    return friend['name']


print(search(friends, 'Anne Pun', get_friend_name))
# start function 'search' with 'finder' as function 'get_friend_name', finder(elem) = get_friend_name(friend),



