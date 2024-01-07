name = input('Whats your name? ')

letter_name = len(name)

if letter_name <= 4:
    print(f'Hello {name}, your name has {letter_name} letters and is short.')
elif letter_name <= 6:
    print(f'Hello {name}, your name has {letter_name} letters and is normal.')
elif letter_name > 6:
    print(f'Hello {name}, your name has {letter_name} letters and is very long.')
