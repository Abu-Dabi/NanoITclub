from random import randint

f = open('../testy/users', 'w')
f.close()
car_dict = {}
ticket = []
print('-' * 30)
print('Computer: Write /help to get help')
help1 = input('You: ')
while help1 != '/help':
    print('Computer: Error! Write /help to get help')
    help1 = input('You: ')
else:
    while True:
        print('-' * 30)
        print('Computer: Write 1 to get new ticket')
        print('Computer: Write 2 to check account')
        print('Computer: Write 3 to close ticket')
        print('Computer: Write 4 to stop program')
        print('-' * 30)
        number = int(input('You: '))
        while number > 4:
            print('Computer: Error! Write only numbers 1 to 3')
            number = int(input('You: '))
        if number == 1:
            ticket.clear()
            random_number = randint(0, 1000)
            ticket.append(random_number)
            users = []
            print("Computer: Write your car's number")
            cars_number = input("You: ")
            car_dict["Car's number"] = cars_number.upper()
            users.append(cars_number.upper())
            print("Computer: Write your car's model")
            cars_model = input("You: ")
            car_dict["Car's model"] = cars_model.upper()
            users.append(cars_model.upper())
            print("Computer: your ticket's number - ", ticket[0])
            car_dict["Your ticket"] = ticket
            users.append(str(ticket))
            f = open('../testy/users', 'a')
            f.write(f"Car's number: {users[0]} \n")
            f.write(f"Car's model: {users[1]} \n")
            f.write(f"Your ticket: {users[2]} \n")
        elif number == 2:
            if ticket == []:
                print("Computer: You don't have ticket")
                print('-' * 30)
                print('Computer: Write /ticket to get ticket')
                ticket1 = input('You: ')
                if ticket1 != '/ticket':
                    print("Computer: Error! Write /ticket to get ticket")
                    ticket1 = input('You: ')
                else:
                    random_number = randint(0, 1000)
                    ticket.append(random_number)
                    users = []
                    print("Computer: Write your car's number")
                    cars_number = input("You: ")
                    car_dict["Car's number"] = cars_number.upper()
                    users.append(cars_number.upper())
                    print("Computer: Write your car's model")
                    cars_model = input("You: ")
                    car_dict["Car's model"] = cars_model.upper()
                    users.append(cars_model.upper())
                    print("Computer: your ticket's number - ", ticket[0])
                    car_dict["Your ticket"] = ticket
                    users.append(str(ticket))
                    f = open('../testy/users', 'a')
                    f.write(f"Car's number: {users[0]} \n")
                    f.write(f"Car's model: {users[1]} \n")
                    f.write(f"Your ticket: {users[2]} \n")
                    print('-' * 30)
            print("Computer: Write your ticket's number")
            tickets_number = int(input("You: "))
            while tickets_number != ticket[0]:
                print("Computer: Error! Try again")
                tickets_number = int(input("You: "))
            else:
                print(f"Computer: Your car {car_dict} in the parking lot")
        elif number == 3:
            if ticket == []:
                print("Computer: You don't have ticket")
                print('-' * 30)
                print('Computer: Write /ticket to get ticket')
                ticket1 = input('You: ')
                if ticket1 != '/ticket':
                    print("Computer: Error! Write /ticket to get ticket")
                    ticket1 = input('You: ')
                else:
                    random_number = randint(0, 1000)
                    ticket.append(random_number)
                    users = []
                    print("Computer: Write your car's number")
                    cars_number = input("You: ")
                    car_dict["Car's number"] = cars_number.upper()
                    users.append(cars_number.upper())
                    print("Computer: Write your car's model")
                    cars_model = input("You: ")
                    car_dict["Car's model"] = cars_model.upper()
                    users.append(cars_model.upper())
                    print("Computer: your ticket's number - ", ticket[0])
                    car_dict["Your ticket"] = ticket
                    users.append(str(ticket))
                    f = open('../testy/users', 'a')
                    f.write(f"Car's number: {users[0]} \n")
                    f.write(f"Car's model: {users[1]} \n")
                    f.write(f"Your ticket: {users[2]} \n")
                    print('-' * 30)
            print("Computer: Write your ticket's number")
            tickets_number = int(input("You: "))
            while tickets_number != ticket[0]:
                print("Computer: Error! Try again")
                tickets_number = int(input("You: "))
            else:
                print("Computer: Write /close to close ticket")
                close = input('You: ')
                ticket.clear()
                while close != '/close':
                    print('Computer: Error! Write /close to close ticket')
                    close = input('You: ')
                else:
                    print('Ticket closed')
        elif number == 4:
            print("Computer: Write /stop to stop program")
            stop = input('You: ')
            while stop != '/stop':
                print('Computer: Error! Write /stop to stop program')
                stop = input('You: ')
            else:
                print('Program stopped')
                break