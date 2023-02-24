a = int(input('Your age: '))
while a < 0:
    print("Your age can't be less than 0")
    a = int(input('Your age'))
else:
    if a <= 12:
        print('child')
    elif 12 < a <= 18:
        print('teenager')
    else:
        print('adult')
