message = ["You are lucky", "Decent", "It's rainy day", "This is good", "Nothing"]


def magicGame():
    import random
    number = random.randint(1, 5)
    print(number)

    for i in range(6):
        if i == number:
            print(message[i-1])



magicGame()