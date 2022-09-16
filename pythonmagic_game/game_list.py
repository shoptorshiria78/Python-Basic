message = ["You are lucky", "Decent", "It's rainy day", "This is good", "Nothing"]


def magicGame():
    import random
    number = random.randint(1, 5)
    print(number)
    if number == 1:
        print(message[0])
    elif number == 2:
        print(message[1])
    elif number == 3:
        print(message[2])
    elif number == 4:
        print(message[3])
    elif number == 5:
        print(message[4])


magicGame()
