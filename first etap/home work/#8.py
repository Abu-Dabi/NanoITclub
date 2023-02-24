print('#' * 30)
a = input('Login:')
b = input('Password:')
print('Repeat your password')
c = input('Password:')
while c != b:
    print('Password unaccepted')
    c = input('Password:')
else:
    print('Password accepted')
print('#' * 30)
