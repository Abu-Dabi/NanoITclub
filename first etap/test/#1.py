def solution(arr):
    count = 1
    names = arr.split()
    first = names[count]
    master = []
    for i in names:
        print (i, first, i[0], first[-1])
        if i[0] == first[-1] and i not in master:
            master.append(i)
            count += 1
            first = i
            return True
        else:
            return False


print(solution(["apple","exercise"]))