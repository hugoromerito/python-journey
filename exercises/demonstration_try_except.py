hour = input('Hello, what time is it? ')

try:
    hour_int = int(hour)

    if hour_int >= 0 and hour_int <= 23:
        if hour_int >= 0 and hour_int <= 11:
            print(f'Its {hour_int}, good morning.')
        elif hour_int >= 12 and hour_int <= 17:
            print(f'Its {hour_int}, good afternoon.')
        else:
            print(f'Its {hour_int}, good night.')
    else:
        print(f'{hour_int}, incorrect time.')

except:
    print('Please enter an integer.')
