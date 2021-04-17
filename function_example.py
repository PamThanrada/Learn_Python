def hello():
    print('Hello', end= '') #end= next line to be one line
    print('Pam')
    print('Hello', 'Hello', 'Hello')
    print('Hello', 'Hello', 'Hello', sep= 'ABC' )

hello()

def multipleFive(number):
    return number * 5

print(multipleFive(20))

newNumber = multipleFive(10)
print(newNumber)