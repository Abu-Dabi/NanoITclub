print('#'*30)
k = int(input())
m = int(input())
n = int(input())

if k >= n:
    x = 2 * m
else:
    x = (2 * n // k) * m
    if n % k != 0 and n % k != k // 2:
        x += m
print(x)
print('#'*30)