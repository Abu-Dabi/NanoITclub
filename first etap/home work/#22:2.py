print('#' * 30)
m = int(input('Number: '))
n = int(input('Number: '))
while m < n:
    print(f"Number must be smaller than {m}")
    n = int(input('Number'))
if m > n:
    print(*range(m, n, -3))
print('#' * 30)

