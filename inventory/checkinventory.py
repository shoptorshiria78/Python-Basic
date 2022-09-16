stuff ={
    "rope" : 10,
    "torch": 10,
    "mobile":20,
    "sim card": 50
}

#total number of item: 4
# total quantity : 100

#for i in stuff.keys():

length = len(stuff.keys())
print(length)

item = 0
for v in stuff.values():

    item += v


print(item)

print(sum(stuff.values()))


def display_inventory():
    print("inventory: ")
    items = len(stuff.keys())
    print("Total number of items:" + str(items))

    item_total=0
    for k, v in stuff.items():
        item_total += v

    print("Total quantity" + str(item_total))

display_inventory()