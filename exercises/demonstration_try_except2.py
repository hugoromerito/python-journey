number_str = input('Enter a number please: ')

try:
    number_int = int(number_str)
    rest = number_int % 2
    if rest == 0:
        print(f'Number {number_int} is even.')
    else:
        print(f'Number {number_int} is odd')
except:
    print(f'Please enter an integer.')
