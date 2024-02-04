from pyfiglet import Figlet
import sys
f = Figlet()
all_fonts = f.getFonts()
print(all_fonts)
if len(sys.argv)==1:
    text = input("Input: ")
    f = Figlet(font='banner3')
    print("Output:")
    print(f.renderText(text))
elif len(sys.argv)==3:
    font_cmd = sys.argv[1]
    font_name = sys.argv[2]
    if(all_fonts.index(font_name)):
        if(font_cmd == "-f" or font_cmd == "--font"):
            text = input("Input: ")
            try:
                f = Figlet(font=font_name)
            except:
                sys.exit("Invalid usage")
            print("Output:")
            print(f.renderText(text))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")




