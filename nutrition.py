def main():
    food = input("Item: ")

    table = [
        {"Name":"apple","Calories":"130"},
        {"Name":"avocado","Calories":"50"},
        {"Name":"banana","Calories":"110"},
        {"Name":"Kiwifruit","Calories":"90"},
        {"Name":"pear","Calories":"100"},
        {"Name":"sweet cherries","Calories":"100"}
    ]

    for x in table:
        if(x["Name"] == food.lower()):
            print("Calories:",x["Calories"])




main()

