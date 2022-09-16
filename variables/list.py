
student1 = ['devid','mail@gmail.com','12345678','dhaka']
student2 = ['smith','smith@gmail.com','12345678','Ny']

print(student1[0])
print(len(student1))

student2_name = student2[0]
print(student2_name)

guest = ['superman','spiderman','batman','ironman','aquaman','naruto','wonder man','wonder women','antman','john snow']
#lunch_guest =[guest[1],guest[5]]
lunch_guest = guest[0:5]
print(lunch_guest)

dinner_guest = guest[5:]
print(dinner_guest)

special_guest = guest[2:4]
print(special_guest)

number = [12,23,42,3,3,44]
number.sort()
print(number)
number.reverse()
print(number)

number.insert(3,10)
print(number)

number.append(100)
print(number)


number.remove(23)
print(number)

number.pop(0)
print(number)

number.clear()
print(number)





