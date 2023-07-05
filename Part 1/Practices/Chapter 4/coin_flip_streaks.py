import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_list = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            coin_list.append('H')
        else:
            coin_list.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streaks = ''
    for index, item in enumerate(coin_list):
        if index == 0:
            streaks += item
            continue
        if item in streaks:
            streaks += item
            if len(streaks) == 6:
                numberOfStreaks += 1
        else:
            streaks = ''
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))