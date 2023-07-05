
grid = [['.', '.', '.', '.', '.', '.'], # 0
        ['.', 'O', 'O', '.', '.', '.'], # 1
        ['O', 'O', 'O', 'O', '.', '.'], # 2
        ['O', 'O', 'O', 'O', 'O', '.'], # 3
        ['.', 'O', 'O', 'O', 'O', 'O'], # 4
        ['O', 'O', 'O', 'O', 'O', '.'], # 5
        ['O', 'O', 'O', 'O', '.', '.'], # 6
        ['.', 'O', 'O', '.', '.', '.'], # 7
        ['.', '.', '.', '.', '.', '.']] # 8 -> width
#         0    1    2    3    4    5 -> height

# 90 degree rotate in clockwise direction

# 9x6 --index--> 8x5
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

WIDTH = 6
HEIGHT = 9

# failed 1
# for x in range(HEIGHT):
#     for y in range(WIDTH):
#         print(grid[x][y], end='')
#     print()

# failed 2
# for x in range(HEIGHT):
#     for y in range(WIDTH):
#         print(grid[y][x], end='')
#     print()

for x in range(WIDTH):
    for y in range(HEIGHT):
        print(grid[y][x], end='')
    print()