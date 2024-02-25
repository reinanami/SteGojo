# assigning all the global variables
X = 490 # Width of the image
Y = 900 # Height of the image
XY = X * Y # Area of the image

# Fetch console design aesthetics from the aesthetics folder
title_file = open("aesthetics/title.txt")
title = title_file.read()
encrypter_aesthetics_file = open("aesthetics/encrypter_aesthetics.txt")
encrypter_aesthetics = encrypter_aesthetics_file.read()
decrypter_aesthetics_file = open("aesthetics/decrypter_aesthetics.txt")
decrypter_aesthetics = decrypter_aesthetics_file.read()
main_aesthetics_file = open("aesthetics/main_aesthetics.txt")
main_aesthetics = main_aesthetics_file.read()
line_file = open("aesthetics/line.txt")
line = line_file.read()
bar_file = open("aesthetics/bars.txt")
bar = bar_file.read()

# Opening the bmp image files
with open("gojo.bmp", "rb") as gojo_bmp_file:
    gojo_bmp = gojo_bmp_file.read()

with open("encryptedgojo.bmp", "rb") as gojo_encrypted_bmp:
    gojo_encrypted_bmp = gojo_encrypted_bmp.read()


def encrypter():
    #Cool aesthetics below
    print(encrypter_aesthetics)
    message = input("| message: ")
    print(bar)
    print(bar)
    print("| Encrypting...")
    
    message_length = len(message) #First we remember the length of our message for later

    metadata = gojo_bmp[:54] #We want to save the metadata so that it saves the bmp file properly
    data = gojo_bmp[54:] #We want to split it so that data can be encrypted without complications

    message_in_binary = ''.join(format(ord(l), '08b') for l in message) #We turn the letters 'l' within the message into 08b format as 1 letter = 8 bits = 1 byte

    byte_array_data = bytearray(data) #We use bytearray so it formats into data[X][Y][ColorPixel]

    index = 0 #initialize index

    for bit in message_in_binary: #For every bit inside the message
        green_index = index * 3 + 1 # We skip to green. 3 serves as an offset

        if bit == '1': #If it matches as one
            byte_array_data[green_index] |= 1 #Bitwise OR 1
        else: #Otherwise
            byte_array_data[green_index] &= ~1 #Bitwise AND not 1 (0)
        index += 1 #We increment 
        print("| " + str(index) + " bits out of " + str(message_length * 8) + " done...") #Bit counter for fun

        if index * 3 >= len(byte_array_data):
            print("| Finished encrypting data...") #Make sure that it doesn't overflow
            break

    print("| Writing data to encrypted gojo image...")

    with open("encryptedgojo.bmp", "wb") as gojo_encrypted_bmp:
        gojo_encrypted_bmp = gojo_encrypted_bmp.write(metadata + byte_array_data) #We write the encrypted bmp onto encrypted gojo bmp
    
    print("| Done!")

    return message_length #Return the message length so that it remembers how to decrypt the message properly 
    

def decrypter(message_length):
    #Cool aesthetics below
    print(decrypter_aesthetics)
    print("| Decrypting...")

    data = gojo_encrypted_bmp[54:] #Split the data from the metadata
    decrypted_message_bin = '' #iitialize the binary string

    byte_array_data = bytearray(data)

    print("| Looksmaxxing...")

    index = 0
    for bit in byte_array_data:
        green_index = index * 3 + 1 # skip to green

        bit = byte_array_data[green_index] &1
        decrypted_message_bin += str(bit)

        index += 1

        if index * 3 >= 24 * message_length: # 3 * 1 byte = 3 * 8 bits, making it 24
            print("| Finished decrypting data...")
            break
    
    print("| Writing message...")

    convert_to_ASCII = [] #using lists to convert the binary into ascii

    for c in range(0, len(decrypted_message_bin), 8):
        convert_to_ASCII += chr(int(decrypted_message_bin[c :c+8], 2)) #Using base2 binary, we sort the binary numbers into 8 bits so that it can be converted into a character

    message = ""

    for char in convert_to_ASCII:
        message += char

    print("| " + message)

#main
print(title)
while True:
    print(main_aesthetics)
    action_response = input("| Your response: ")
    print(line)
    if action_response == "E":
        message_length_num = encrypter()
        message_length = str(message_length_num)
        print(line)
        with open("message_length.txt", "w") as message_length_file:
            message_length_update = message_length_file.write(message_length) #We want to secure the message length
        break
    if action_response == "D":
        with open("message_length.txt", "r") as message_length_file:
            message_length_input = message_length_file.read() #We want to read the message length so that we decrypt the right size
        message_length_input_int = int(message_length_input)
        decrypter(message_length_input_int)
        print(line)
        break
    if action_response == "README":
        readme_file = open("readme.txt") #Readme to document commands and important information
        readme = readme_file.read()
        print(readme)
    if action_response == "You are my special.":
        secret_file = open("aesthetics/secret.txt")
        secret = secret_file.read()
        print(secret)
    else:
        print("| Unknown command detected. Please try again!                                 |") #This code constitutes an error due to an unknown command
        print(line)