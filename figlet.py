from pyfiglet import Figlet
import sys



if len(sys.argv)==0:
    text = input("Input: ")
    f = Figlet(font='banner3')
    print(f.renderText(text))





