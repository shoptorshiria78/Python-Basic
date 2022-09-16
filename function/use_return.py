def get_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f" {first_name} {middle_name} {last_name}"
    else:
        full_name = f" {first_name} {last_name}"
    return full_name.title()


musician = get_name('karim', 'khan', )

print(musician)


def build_person(first_name, last_name):
    '''buildin a dictionary named person'''
    person = {'first': first_name, 'last': last_name}
    return person


dc_name = build_person('lina', 'rina')
print(dc_name)


def build_profile(first_name, last_name, occupassion, age):
    '''building a dictionary named profile'''
    profile = {'first': first_name.title(), 'last': last_name.title(), 'profession': occupassion.title(), 'years': age}
    #    if occupassion:
    #        profile['profession'] = occupassion

    #    if age:
    #        profile['years'] = age


# return profile


# print('write your first name, last name, occupassion, age')
# biography = build_profile('raju', 'mia', 'student', '17')

# print(biography)

#def build_n(f_name, l_name):
#    '''building a name given by the programmer using while loop'''
#    formatted_name = f" {f_name} {l_name}"
#    return formatted_name


#'''taking input from programmer'''
#while True:
#    print('write your first name and last name.')
#    print('(enter "quit" if you want to stop the program)')

#    f_name = input('what is your first name?')
#    if f_name == 'quit':
#        break
#    l_name = input('what is your last name?')
#    if l_name == 'quit':
#        break

#    programmer_name = build_n(f_name, l_name)
#    print(programmer_name)


def list_greets(names):
    '''collections of name will pass through here'''
    for name in names:
        print(f"Hello!, {name.title()}")

user_names = []

while True:
    take_name = input("write a name:")
    print('if you want to stop the program write "quit".')
    if take_name == "quit":
        break
    user_names.append(take_name.title())
print(user_names)
print(list_greets(user_names))

