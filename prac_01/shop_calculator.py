item1 = float(input("Enter price of item 1: $"))
item2 = float(input("Enter price of item 2: $"))
item3 = float(input("Enter price of item 3: $"))
total = item1 + item2 +item3

if total <= 0:
    print("invalid number of items")

elif total > 100:
    print("The total is $",total * 0.9)

else:
    print("The bonus is $",total)