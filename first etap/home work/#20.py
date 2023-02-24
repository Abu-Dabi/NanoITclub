print('#'*30)
a = input('Number: ')
b = 0
while int(a) <= 0:
    print('Number must be more than 0')
    a = input('Number: ')
else:
    for i in a:
        b = b + int(i)
print(b)
print('#'*30)
