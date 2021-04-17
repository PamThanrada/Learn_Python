import random
print('Hello, What is your name?')
name = input()
print('Ok ' + name + ' I am thinking of a number between 1 to 10.')
print('Please, Guess the number.')

secretNumber = random.randint(1, 10)

for guessTaken in range(1, 8):       #You can guess 7 times.
    GuessNumber = int(input())
    if GuessNumber > secretNumber:
        print('It is high number.')
    elif GuessNumber < secretNumber:
        print('It is low number.')
    else:
        break

if GuessNumber == secretNumber:
    print('True ' + name + ' You can guessed the number.')
else:
    print('The number I was thinking is ' + str(secretNumber))

