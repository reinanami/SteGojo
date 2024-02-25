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

#Fetch aesthetics from txt files
title_file = open("aesthetics/title.txt")
title = title_file.read()
encrypter_aesthetics_file = open("aesthetics/encrypter_aesthetics.txt")
encrypter_aesthetics = encrypter_aesthetics_file.read()
main_aesthetics_file = open("aesthetics/main_aesthetics.txt")
main_aesthetics = main_aesthetics_file.read()
line_file = open("aesthetics/line.txt")
line = line_file.read()

def encrypter():
    #Cool aesthetics below
    print(encrypter_aesthetics)
    message = input("| message: ")
    print("|                                                                             |")
    print("|                                                                             |")
    print("| Encrypting...                                                               |")
    
    #Encrypt here
    

def decrypter():
    #Decrypt here
    print("WIP")

def help_page():
    print(line)
    print("|                                                                             |")
    
#main
print(title)
while True:
    print(main_aesthetics)
    action_response = input("| Your response: ")
    print(line)
    if action_response == "E":
        encrypter()
        print(line)
    if action_response == "D":
        decrypter()
        print(line)
    if action_response == "H":
        help_page()
    if action_response == "README":
        readme_file = open("readme.txt")
        readme = readme_file.read()
        print(readme)
    else:
        print("| Unknown command detected. Please try again!                                 |")
        print("| Type 'H' for help                                                           |")
        print(line)