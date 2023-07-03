
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    
number = 1 

try:
    number = int(input('Enter number: '))
except ValueError:
    print('You must enter integer value: ') #TODO: change this.

while number != 1:
    number = collatz(number)
    print(number)

