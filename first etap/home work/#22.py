print('#' * 30)
m = int(input('Number: '))
n = int(input('Number: '))
while m < n:
    print(f"Number must be smaller than {m}")
    n = int(input('Number'))
for i in range(m, n, -3):
    print(i)
print('#' * 30)
