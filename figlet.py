from pyfiglet import Figlet
import sys



if len(sys.argv)==1:
    text = input("Input: ")
    f = Figlet(font='banner3')
    print(f.renderText(text))





