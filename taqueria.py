menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
i=0
j=0
sum=0
while True:
    try:
        item = input("Item: ")
        for i in menu:
            if i.lower() == item.lower():
                sum  += float(menu[i])
                print(f"Total: ${sum}")
    except EOFError:
        print()
        break


