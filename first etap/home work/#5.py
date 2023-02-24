print('write even number to kill everyone')
print('write odd number to save half of the people')
n = int(input('population:'))
a = n % 2
if a==0:
    print('You kill everyone')
else:
    print('Good you save half of the people:',int(n/2+0.5))
