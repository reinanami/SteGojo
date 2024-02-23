# assigning all the global variables
RED = 0xFF0000
BLUE = 0x00FF00
GREEN = 0x0000FF
MAX = 0xFFFFFF
MIN = 0x000000

#Gojo image processor
IMGWIDTH = 0x1CD
IMGHEIGH = 0x384
X = 0x19
Y = 0x19


def encrypter():
    #Cool aesthetics below
    print("-----S-T-E-G-A-N-O-G-R-A-P-H-Y---E-N-C-R-Y-P-T-E-R-----")
    print("|                                                     |")
    print("|                                                     |")
    print("| ----- Please type the message -----                 |")
    message = input("| message: ")
    print("|                                                     |")
    print("|                                                     |")
    print("| Encrypting...                                       |")
    
    #Encrypt here
    

def decrypter():
    #Decrypt here
    print("WIP")

def help_page():
    print("-----------------------Help Desk-----------------------")
    print("|                                                     |")
    
#main
while True:
    print(">>>>>>>>>>>>>>>>>>Welcome-to-SteGojo!<<<<<<<<<<<<<<<<<<")
    print("|        TYPE 'H' FOR HELP, TYPE README FOR MORE      |")
    print("| Loading...                                          |")
    print("| Would you like to encrypt'E' or decrypt'D'?:        |")
    action_response = input("| Your response: ")
    if action_response == "E":
        encrypter()
        print("-------------------------------------------------------")
    if action_response == "D":
        decrypter()
        print("-------------------------------------------------------")
    if action_response == "H":
        help_page()
    if action_response == "README":
        file = open("readme.txt")
        documentation = file.read()
        print(documentation)
    else:
        print("| An unknown error had occured. Please try again!     |")
        print("| Type 'H' for help                                   |")
        print("-------------------------------------------------------")    
        break
