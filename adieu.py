import inflect

p  = inflect.engine()
list = []
while True:
    try:
        name = input("Name: ")
        list.insert(name)
    except EOFError:
        break

mylist = p.join(list)
print(mylist)
