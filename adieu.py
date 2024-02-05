import inflect

p  = inflect.engine()
list = ["Adieu, adieu, to "]
while True:
    try:
        name = input("Name: ")
        list.append(name)
    except EOFError:
        break

mylist = p.join(list)
print(mylist)
