f = open('score.rp', 'w')
score = {'user': 0}
f.close()

f = open('score.rp', 'a')
score['user'] += 1
print(f)
