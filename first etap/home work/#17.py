print('#' * 30)
a = int(input('How much money do you want to save:'))
c = 0
while c < a:
    print('Piggy bank:', c)
    b = int(input('Put money:'))
    if b<0:
        print("You can't take money from piggy bank")
    else:
        c = c + b
else:
    print('Your piggy bank is full')
    print('You save', c, 'money')
print('#' * 30)