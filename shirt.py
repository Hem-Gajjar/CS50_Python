import sys
from PIL import Image,ImageOps

count = len(sys.argv)

if count < 3:
    sys.exit("Too few command-line arguments")
elif count > 3:
    sys.exit("Too many command-line arguments")

filename1 = sys.argv[1]
filename2 = sys.argv[2]

try:
    name1,ext1 = filename1.split(".")
    name2,ext2 = filename2.split(".")
except:
    sys.exit("Invalid input")

ext1 = ext1.lower()
ext2 = ext2.lower()


if ext1 == "jpg" or ext1 == "jpeg" or ext1 == "png" or ext2 == "jpg" or ext2 == "jpeg" or ext2 == "png":
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    else:
        # open both files
        man = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        # resize file
        size = shirt.size
        man = man.resize(size)
        # overlay file
        man.paste(shirt,(0,0),mask=shirt)
        name = sys.argv[2]
        man.save(
            name,save_all=True
        )
else:
    sys.exit("Invalid input")
# ***************************
# import sys

# from PIL import Image

# images= []

# for arg in sys.argv[1:]:
#     image= Image.open(arg)
#     images.append(image)

# images[0].save(
#     "bird.gif" , save_all=True, append_images=[images[1]],duration=200,loop=0
# )
