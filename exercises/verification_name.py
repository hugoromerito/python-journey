name = input('Hello, enter your name: ')
age = input(f'Coll {name}, now enter your age: ')

if len(name) == 0 or len(age) == 0:
    print('Sorry, you left fields empty!')
else:
    if ' ' in name:
        verification_space = 'Your name contains spaces'
    else:
        verification_space = 'Your name does not contains spaces'

    print(f'His name is {name}')
    print(f'His reversed name is {name[::-1]}')
    print(verification_space)
    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is {name[:1]}')
    print(f'The last letter of your name is {name[-1:]}')
