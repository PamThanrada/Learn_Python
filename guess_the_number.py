import random
print('Hello, What is your name?')
name = input()
print('Ok ' + name + ' I am thinking of a number between 1 to 10.')

secretNumber = random.randint(1, 10)

for guessTaken in range(1, 8):       #You can guess 7 times.
    print('Please, Guess the number')
    GuessNumber = int(input())
    if GuessNumber > secretNumber:
        print('It is high number.')
    elif GuessNumber < secretNumber:
        print('It is low number.')
    else:
        break

if GuessNumber == secretNumber:
    print('True ' + name + ' You can guessed the number in ' + str(guessTaken) + ' gresses.')
else:
    print('The number I was thinking of was ' + str(secretNumber))

