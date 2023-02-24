print('#'*30)
a = int(input("Cabin's number:"))
if 0 < a <= 36:
    print("Compartment's number:",(a - 1) // 4 + 1)
else:
    print('Fail')
print('#'*30)
