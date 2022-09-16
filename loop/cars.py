cars = ["toyota", "audi", "subaru", "bmw"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

answer = 17
if answer != 42:
    print("the answer is not correct")



banned_users = ['karim', 'rahim', 'jomila', 'romola']
user = 'karim'

if user not in banned_users:
    print(f" {user.title()} you can post anything you want.")

else:
    print(f" {user.title()} you are not allowed to post anything")

