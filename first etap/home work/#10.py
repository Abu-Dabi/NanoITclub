print('#' * 30)
a = input('Programming language:')
b = int(input('Age:'))
c = int(input('Work experience in years:'))
d = int(input('Salary:'))
print('#'*30)
if a == 'java' or a == 'python' or a == 'javascript':
    print('Programming language:',' Accepted')
else:
    print('Programming language:',' Unaccepted')
if 17 < b < 66:
    print('Age:',' Accepted')
else:
    print('Age:',' Unaccepted')
if 3 < c:
    print('Work experience in years:',' Accepted')
else:
    print('Work experience in years:',' Unaccepted')
if 0 < d < 60001:
    print('Salary:', ' Accepted')
else:
    print('Salary:', ' Unaccepted')
print('#'*30)
print("If you don't have 'Unaccepted', you have hired")
print("If you have 'Unaccepted', you don't have hired")
print('#'*30)

