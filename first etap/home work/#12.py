print('#'*30)
a=int(input('Number #1:'))
b=int(input('Number #2:'))
c=int(input('Number #3:'))
d=int(input('Number #4:'))
print('#'*30)
if a<b and a<c and a<d:
    print('#1',a,'smallest number')
elif b<a and b<c and b<d:
    print('#2',b, 'smallest number')
elif c<b and c<a and c<d:
    print('#3',c, 'smallest number')
elif d<b and d<c and d<a:
    print('#4',d, 'smallest number')
print('#'*30)