# Short program to test out the syntax for formatting strings that are output from the print command()

# Author: Gerry Donnelly

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

format = color()

print ('\033[4m' + '\033[92m' + "Hello World" + '\033[0m')

print ("Please enter your" + format.BOLD + format.UNDERLINE + format.YELLOW + " Hello World" + format.END)