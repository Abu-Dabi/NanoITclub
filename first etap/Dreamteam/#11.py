numbers = [2, 4, 7, 1, 8.4, -3.3, 7.1, -2, 4, -1, 7, -43, 8, -3, 6, 9]
a = [x for x in numbers if x % 2 == 0]
print('even number: ',len(a))
b = [x for x in numbers if x % 2 != 0]
print('odd numbers',len(b))

