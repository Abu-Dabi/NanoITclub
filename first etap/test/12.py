
login_passwords = {'Abu': '1234',
                   'Sulaiman': '4321',
                   'Magamed': '2020',
                   'Dastan': '1010'}
a = ''
b = ''
c = input('Login: ')
if c in login_passwords:
    print('Login exist')
    t = ''.join(c)
    key = login_passwords.get(t)
    print(key)