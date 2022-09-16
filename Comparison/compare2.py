name = ''
password = ''

while name != 'superman' and password != 'superhero':
    print('please enter your name and password:')
    name = input()
    password = input()

    if name == 'superman' and password == 'superhero':
          print("thank you. access granted")
    else:
          print("access rejected. please try again")

    continue