import pyinputplus as pyip
import random

'''
Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
'''

BREAD_TYPE = ['wheat', 'white', 'sourdough']
PROTEIN_TYPE = ['chicken', 'turkey', 'hame', 'tofu']
CHEESE_TYPE = ['cheddar', 'swiss', 'mozzarella']

totalCost = 0

bread = pyip.inputMenu(BREAD_TYPE, '# Which bread type do you want?\n', numbered=True)
bread_price = random.randint(1,10)
print(f'-> You choose {bread} bread - {bread_price}$')
print('-'*20)

protein = pyip.inputMenu(PROTEIN_TYPE, '# Which protein type do you want?\n', numbered=True)
protein_price = random.randint(1,10)
print(f'-> You choose {protein} protein - {protein_price}$')
print('-'*20)

cheese_price = 0
want_cheese = pyip.inputYesNo('# Do you want cheese?\n')
if want_cheese == 'yes':
    cheese = pyip.inputMenu(CHEESE_TYPE, '# Which cheese type do you want?\n', numbered=True)
    cheese_price = random.randint(1,10)
    print(f'-> You choose {protein} cheese - {cheese_price}$')
    print('-'*20)
    
item_total_price = 0
for item in ['mayo', 'mustard', 'lettuce', 'tomato']:
    want_item = pyip.inputYesNo(f'# Do you want {item} in your sandwich?\n')
    if want_item == 'yes':
        item_price = random.randint(1,10)
        print(f'-> You want {item} - {item_price}$')
        item_total_price += item_price
        print('-'*20)

sandwich_count = pyip.inputInt('# How many sandwiches do you want?\n')

totalCost = (bread_price + protein_price + cheese_price + item_total_price) * sandwich_count

print(f'---> Your total cost is {totalCost}$ :D')