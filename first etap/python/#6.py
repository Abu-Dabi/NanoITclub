a=int(input('a equals'))
b=int(input('b equals'))
c=int(input('c equals'))
if a>b and a>c:
    print('a biggest')
elif a<b and a<c:
    print('a smallest')
if b>a and b>c:
    print('b biggest')
elif b<a and b<c:
    print('b smallest')
if c>b and c>a:
    print('c biggest')
elif c<b and c<a:
    print('c smallest')