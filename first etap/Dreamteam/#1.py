c = range(0,1000)
a = ([x for x in c if x % 3 == 0])
b = ([x for x in c if x % 5 == 0])
x = (a+b)
d = sum(x)
print(d)

