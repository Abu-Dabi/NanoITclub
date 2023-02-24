for i in range(6):
    print('#' * 30)
    print('write 1 to add new city')
    print('write 2 to get list of cities')
    print('write 3 to replace city')
    print('write 4 to delete city')
    print('write 5 to exit')
    print('#' * 30)
    list = ['New-York', 'Bishkek', 'Moskva', 'Almaty']
    a = int(input('Number: '))
    while a > 6:
        print('Fail! Try again')
        a = int(input('Number: '))
    if a == 1:
        b = input('New city: ')
        if b not in list:
            print('City added')
        elif b in list:
            print(f"City already in list!{b}")
        else:
            print('Incorrect')
        list.append(b)
    if a == 2:
        list.append(b)
        print('List of cities: ', list)
    if a == 3:
        list.append(b)
        print('Which city you want to change')
        print(list)
        OldCity = input("City's name: ")
        while OldCity not in list:
            print(f"{OldCity} not in the list")
        else:
            print(f"{OldCity} in the list")
        Newcity1 = input("New city's name: ")
        if Newcity1 in list:
            print(F"{Newcity1} already in list")
        elif Newcity1 not in list:
            print('City replaced')
        else:
            print('Incorrect')
        list.remove(OldCity)
        list.append(Newcity1)
        print(list)
    if a == 4:
        list.append(b)
        list.remove(OldCity)
        list.append(Newcity1)
        t = input('Delete city: ')
        if t not in list:
            print("City not in list")
        elif t in list:
            print('You deleted city')
        else:
            print('Incorrect')
        list.remove(t)
        print(list)
    if a == 5:
        print('End')
        break

# Работает только если выбирать по очереди
# По другому не смог
