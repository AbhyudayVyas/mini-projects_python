import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
font_list = []
font_list =  figlet.getFonts()

# print(font_list)

try:
    if  sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in font_list:
            figlet.setFont(font=sys.argv[2])
        else:
            print("invalid usage")
            sys.exit()
    else:
        print("invalid usage")
        sys.exit()
except IndexError:
    figlet.setFont(font=random.choice(font_list))

text = input("Input: ")
print(f"Output: \n {figlet.renderText(text)}")