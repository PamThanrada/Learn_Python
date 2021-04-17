def div80by(divideby):
    try:
        return 80 / divideby
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')

print(div80by(10))
print(div80by(20))
print(div80by(0))
print(div80by(1))
