birthdays = { "Alice": "2 may","Bob":" 7 mar", "karim": "28 june", "rahim": "10 jan" }

name = input(" Tell a name:")

if name in birthdays.keys():

    print(birthdays[name])

else:
    print("Invalid name")


