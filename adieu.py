import inflect

p  = inflect.engine()


while True:
    try:
        name = input("Name: ")
        mylist = p.join(name)
    except EOFError:
        break

print(mylist)
