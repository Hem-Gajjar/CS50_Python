str = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
str = str.lower()
str = str.strip()
if(str == "42"):
    print("Yes")
elif(str == "forty two"):
    print("Yes")
elif(str == "forty-two"):
    print("Yes")
else:
    print("No")

