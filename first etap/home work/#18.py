print('#'*30)
n = int(input('Number: '))
x = 1
while n > 12:
    print('Number must be less than 12')
    n = int(input('Number: '))
for i in range(1, n + 1):
    x = x * i
    print(str(i),"!=",x)
print('#'*30)