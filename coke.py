

price = 50
amount=0
while True:
    coin = int(input("Insert Coin: "))
    if coin == 25:
        amount += 25
    elif coin == 10:
        amount +=10
    elif coin == 5:
        amount +=5

    print("Amount Due:",price-amount)
    if amount == price:
        print("Change Owed:",price-amount)
        break
    elif amount > price:
        print("Change Owed:",amount-price)
        break
