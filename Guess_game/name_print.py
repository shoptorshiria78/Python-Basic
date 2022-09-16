#name = "riziya akter keya"

#for call in range(10):
#    print(name)

#class Restaurent:

#    def __init__(self, restaurent_name, restaurent_cuisine):

#        self.restaurent_name = restaurent_name#        self.restaurent_cuisine = restaurent_cuisine

#    def describe_restaurent(self):
#        print(f"the restaurent name is {self.restaurent_name} ")
#        print(f" the restaurent cuisine is {self.restaurent_cuisine}")

#    def open_restaurent(self):
#        print("restaurent open at 2.00 PM")

#    def close_restaurent(self):
#        print("restaurent close at 11.00 PM")


#my_restaurent = Restaurent("keya's kitchen", "Indian")

#name = my_restaurent.restaurent_name
#print(name)
#cuisine = my_restaurent.restaurent_cuisine
#print(cuisine)
#my_restaurent.describe_restaurent()
#my_restaurent.open_restaurent()
#my_restaurent.close_restaurent()


class Car:

    def __init__(self,make , model, year):

        self.make = make
        self.model = model
        self. year = year
        self.odometer_reading = 500

    def descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name



    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage

        else:
            print("You cannot roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


    def read_odometer(self):
        print(f"the odometer reading of the car is {self.odometer_reading}")


my_car = Car("toyota", "alion", "2019")
print(my_car.descriptive_name())
#my_car.odometer_reading = 23
my_car.update_odometer(50)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()

class ElectricCar(Car):


    def __init__(self, make, model, year):

        super().__init__(make, model, year)
        self.battery_size = 75

    def battery(self):
        print(f"the size of the battery of this class is {self.battery_size} ")


my_tesla = ElectricCar("Tesla", "model s", "2019")

print(my_tesla.descriptive_name())

my_tesla.battery()
