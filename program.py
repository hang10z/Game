import random

print('--------------------------------------------------')
print('     GUESS THAT NUMBER GAME')
print('--------------------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
player_name = input('Hello, please enter your name...')

while guess != the_number:
    guess_text = input('Hi {0}! Guess the number between 0 and 100: '.format(player_name))

    guess = int(guess_text)

    if guess < the_number:
        # The .format at the end passes guess and player_name variables to the {} in the below string
        print('Sorry {1}, Your guess of {0} was too LOW'.format(guess, player_name))
    elif guess > the_number:
        print('Sorry {1}, your guess of {0} was too HIGH'.format(guess, player_name))
    else:
        print("Great Job {1}! You've guessed the number!".format(guess, player_name))

print('done')
