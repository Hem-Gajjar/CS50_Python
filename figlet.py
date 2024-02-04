from pyfiglet import Figlet
import sys



if len(sys.argv)==1:
    text = input("Input: ")
    f = Figlet(font='banner3')
    print(f.renderText(text))

if len(sys.argv)==3:
    font_cmd = sys.argv[1]
    font_name = sys.argv[2]
    if(font_cmd == "-f" or font_cmd == "--font"):
        text = input("Input: ")
        f = Figlet(font=font_name)
        print(f.renderText(text))





