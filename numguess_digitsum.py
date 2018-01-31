'''
from random import randint

random_number = randint(1, 10)
print(random_number)
guesses_left = 3
while guesses_left > 0:
    guess = int(input("Guess the number : "))
    if guess == random_number:
        print("You win!")
        break
    else:
        guesses_left-=1
        if guesses_left == 0:
            print("You lose")
'''

def digit_sum(n):
    sum = 0
    while 1:
        if n//10 == 0:
            sum += n%10
            return sum
            break
        elif n//10 > 0:
            sum += n%10
            n = n//10

def digit_sumsum(n):
    a = str(n)
    sum = 0
    for i in a:
        sum += int(i)
    return sum
        
print(digit_sum(1234))
print(digit_sumsum(1234))
