alien_color =  'red'

if alien_color == 'green':
     print('the player just earn 5 points')
else:
    print ('the player just earn 10 points')


age= 67

if age<2 :
    print("the person is baby")
elif age>=2 and age<4 :
    print("the person is toddler")

elif age>=4 and age<13 :
    print("the person is kid")

elif age>=13 and age<20 :
    print("the person is teenager")

elif age>=20 and age<65 :
    print("the person is adult")

elif age>=65  :
    print("the person is elder")

favourite_fruit = ['banana', 'orange', 'pomgrenat']

if 'banana' in favourite_fruit :
       print(" you really likes banana")

if 'orange' in favourite_fruit :
       print(" you really like orange")


requested_topings = ['mashroom','green onion', 'extra cheese', 'green peperoni']

for requested_topping in requested_topings :


      if requested_topping == "green peperoni" :
          print (f" we can not add {requested_topping} now")

      else:
          print(f"Adding {requested_topping}.")

print("\n the pizza is finished")



#make aliens to get in the empty list

aliens = []

for alien_number in range(30):
    new_alien = {
        'color' : 'green',
        'speed' : 'slow',
        'points': '5',
    }
    aliens.append(new_alien)

for alien in aliens[:5] :
    print(alien)

print(aliens)
