print('#'*30)
from random import randint

answers = 10
print('')
for i in range(10):
    a = randint(2, 9)
    b = randint(2, 9)
    c = a * b
    print(f"{a}*{b}=", end=" ")
    answer = int(input(''))
    if answer != c:
        print(f"False! {a}*{b}={c}")
        answers = answers - 1
print(f"True answers: {answers}")
if answers == 0:
    print("Your result: 0%")
if answers == 1:
    print("Your result: 10%")
if answers == 2:
    print("Your result: 20%")
if answers == 3:
    print("Your result: 30%")
if answers == 4:
    print("Your result: 40%")
if answers == 5:
    print("Your result: 50%")
if answers == 6:
    print("Your result: 60%")
if answers == 7:
    print("Your result: 70%")
if answers == 8:
    print("Your result: 80%")
if answers == 9:
    print("Your result: 90%")
if answers == 10:
    print("Your result: 100%")
print('#'*30)
