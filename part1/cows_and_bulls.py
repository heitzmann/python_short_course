import random

pwd = ''
while len(set(pwd)) < 4:
    pwd = '{:04d}'.format(random.randint(0, 9999))
guess = ''
while guess != pwd:
    guess = input('Guess: ')
    if len(guess) == len(pwd):
        pos = sum(guess[i] == pwd[i] for i in range(len(pwd)))
        pwdlist = list(pwd)
        for l in guess:
            if l in pwdlist:
                pwdlist.remove(l)
        sym = len(pwd) - len(pwdlist) - pos
        print(f'{pos} correct positions, {sym} correct digits.')
    else:
        print(f'Your guess must have {len(pwd)} digits.')
print('Correct! You win!')
