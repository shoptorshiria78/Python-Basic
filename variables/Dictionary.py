

#simple Dictionary
car={
    'make':'bmw',
    'model':'bw22',
    'year':2022
}
#Nested dictionary
user={
    'name':'smith',
    'age':'30',
    'location':
        {
            'present address':{
                'house': 42,
                'road': 6,
            },
            'permanent address': 'CTG'
        }
}

print(car['model'])

print(user['location'] ['present address'] ['road'])
print(car.values())
print(user['location'] ['present address'] ['house'])

person = {
    'first_name':'lina',
    'last_name':'khan',
    'age':40,
    'city':'dhaka'
}
print(person['city'])

favourite_color={
    "smith's":'red',
    "kevin's":'blue',
     "devid's":'green'
}
#smith's favourite color is red
#smith's favourite color is red
#smith's favourite color is red
for name in favourite_color.keys():
    print(name.title())
for color in favourite_color.values():
    print(color.title())
for name, color in favourite_color.items():
    print(f"{name.title()}'s favourite color is {color.title()}.")



alien_0 = {'color': 'green', 'point': 5, 'moving': 'forward', 'x_position': 25}
alien_0['y_position']=45
print(alien_0)

alien_0={'x_position':2, "y_position":25, 'speed':'fast'}
print(f"the original x_position of the alien_0: {alien_0['x_position']}")

alien_0['location'] = 'dhaka'

print(alien_0)

if alien_0['speed'] == 'medium':
    x_increment = 4

elif alien_0['speed'] == 'fast':
    x_increment = 6

else:
    x_increment = 8
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"the changed position of the alien_0:{alien_0['x_position']}")

favourite_languages = {
     'jenny' : 'C',
     'jhon' : 'ruby',
     'ekic' : 'python',
      'anik': 'lua',

}

for name,language in sorted(favourite_languages.items()):
    print(f" {name.title()} loves {language.title()} language.")