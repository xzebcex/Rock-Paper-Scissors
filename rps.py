# Rock Paper Scissors.

import random
import sys

wins = 0
losses = 0
ties = 0

while True:  # Main game loop.
    print('%s wins, %slosses, %sties' % (wins, losses, ties))

    while True:  # player input loop.
        player_move = input(
            'Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')
        if player_move == 'q':
            sys.exit()  # Quit the game.

        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break  # Break out of input loop
        print('Type one of r, p, s, or q.')

    # Display's what player chose.
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display's what computer chose.
    random_number = random.randint(1, 3)
    if random_number == 1:
        bot = 'r'
        print('ROCK')
    elif random_number == 2:
        bot = 'p'
        print('PAPER')
    elif random_number == 2:
        bot = 's'
        print('SCISORSS')

    # Display's and record the win/losses/ties.
    if player_move == bot:
        print('It\'s a tie!')
        ties += 1
    elif player_move == 'r' and bot == 's':
        print('You win')
        wins += 1
    elif player_move == 'p' and bot == 'r':
        print('You win:)')
        wins += 1
    elif player_move == 's' and bot == 'p':
        print('You win!')
        wins += 1
    elif player_move == 'r' and bot == 'p':
        print('You lose')
        losses += 1
    elif player_move == 'p' and bot == 's':
        print('you lose')
        losses += 1
    elif player_move == 's' and bot == 'r':
        print('you lose')
        losses += 1
