import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.info(f'user input: {guess}, type: {type(guess)}')

toss = 'heads' if random.randint(0, 1) else 'tails' # 0 is tails, 1 is heads

if toss == guess:
    print('You got it!')
    logging.info(f'user guess: {guess}, toss: {toss}')
else:
    print('Nope! Guess again!')
    guess = input() # HEHE :D
    logging.info(f'user guess: {guess}, toss: {toss}')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        