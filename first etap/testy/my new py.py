f = open('database.txt', 'w')
print('#'*30)
print('Write 1 to log in')
print('Write 2 to sign in')
num = int(input('Write number: '))
while num > 2:
    print('Fail! Try again')
    num = int(input('Number: '))
login_passwords = {'Abu': '1234',
                   'Sulaiman': '4321',
                   'Magamed': '2020',
                   'Dastan': '1010'}
a = ''
b = ''
if num == 1:
    c = input('Login: ')
    while c not in login_passwords:
        print('Error! False login')
        c = input('Login: ')
    else:
        print('Login exist')
        print('#' * 30)
        t = ''.join(c)
        key = login_passwords.get(t)
        print('Write password')
        d = input('Password: ')
        while d != key:
            print('Error! False password')
            d = input('Password: ')
        else:
            print('You log in')
        print('#' * 30)

f.close()
if num == 2:
    c = input('Login: ')
    if c in login_passwords:
        print('Login already exist')
    else:
        f = open('database.txt', 'a')
        print('New login')
        print('#' * 30)
        x = input('Password:')
        print('Repeat your password')
        p = input('Password:')
        while p != x:
            print('Password unaccepted')
            p = input('Password:')
        else:
            print('Password accepted')
        a = ''.join(c)
        v = ''.join(x)
        login_passwords = ['Login: Abu', 'Password: 1234', 'Login: Sulaiman', 'Password: 4321', 'Login: Magamed',
                           'Password: 2020', 'Login: Dastan', 'Password: 1010']
        for x in login_passwords:
            f.write(x + '\n')
        f.write(f"Login: {a}\nPassword: {v}")
        print('You sign in')
        print('#' * 30)
        f.close()
