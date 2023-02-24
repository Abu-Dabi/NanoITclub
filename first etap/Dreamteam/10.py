a = input('Write sentence: ')
b = a.split(" ")
while len(b) < 6:
    print('Sentence must be mor than 6 words!')
    a = input('Write sentence: ')
    b = a.split(" ")
if len(b) % 2 == 0:
    c = len(b) // 2
    d = b[0:c]
    x = b[c:len(b) - 1]
    print(d)
    print(x)
if len(b) % 2 != 0:
    c = len(b) // 2
    d = b[0:c]
    x = b[c:len(b) - 1]
    print(d)
    print(x)
