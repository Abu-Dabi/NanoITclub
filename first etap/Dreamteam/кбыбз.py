while True:
    import random
    print("Write rock, scissors or paper")
    x = input('Write here: ')
    test_list = ['rock', 'scissors', 'paper']
    while x not in test_list:
        print(f"Error!Write only rock, scissors or paper")
        x = input('Write here: ')
    random_index = random.randrange(len(test_list))
    print("Enemy: ", test_list[random_index])
    if x == 'rock' and test_list[random_index] == 'paper':
        print('You lose')
    elif x == 'rock' and test_list[random_index] == 'scissors':
        print('You win')
    elif x == 'rock' and test_list[random_index] == 'rock':
        print('Draw')
    if x == 'paper' and test_list[random_index] == 'scissors':
        print('You lose')
    elif x == 'paper' and test_list[random_index] == 'rock':
        print('You win')
    elif x == 'paper' and test_list[random_index] == 'paper':
        print('Draw')
    if x == 'scissors' and test_list[random_index] == 'rock':
        print('You lose')
    elif x == 'scissors' and test_list[random_index] == 'paper':
        print('You win')
    elif x == 'scissors' and test_list[random_index] == 'scissors':
        print('Draw')