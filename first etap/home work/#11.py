print('#' * 30)
print('Write four-digit number')
a = int(input('Number: '))
t = 999
y = 10000
while t >= a:
    print('Error please try again')
    a = int(input('Number: '))
while a >= y:
    print('Error please try again')
    a = int(input('Number: '))
else:
    print('You can continue')
x = str(a)
b = int(x[0])
c = int(x[1])
d = int(x[2])
e = int(x[-1])
if b + e == c - d:
    print(b, '+', e, '=', '=', c, '-', d)
else:
    print(b, '+', e, '!', '=', c, '-', d)

