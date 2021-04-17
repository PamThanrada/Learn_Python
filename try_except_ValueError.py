print('How many pen do you have?')
numPen = input()
try:
    if int(numPen) >= 10:
        print('There is a lot of pens')
    else:
        print('Nothing much')
except ValueError:
    print('Please, Enter a number')