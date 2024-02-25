import numpy as np

# assigning all the global variables
MAX = 0xFFFFFF
MIN = 0x000000

#Gojo image processor
X = 490
Y = 900
XY = X * Y

#Fetch aesthetics from txt files
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

with open("gojo.bmp", "rb") as gojo_bmp_file:
    gojo_bmp = gojo_bmp_file.read()

with open("encryptedgojo.bmp", "rb") as gojo_encrypted_bmp:
    gojo_encrypted_bmp = gojo_encrypted_bmp.read()


def encrypter():
    #Cool aesthetics below
    print(encrypter_aesthetics)
    message = input("| message: ")
    print("|                                                                             |")
    print("|                                                                             |")
    print("| Encrypting...                                                               |")
    
    message_length = len(message)

    metadata = gojo_bmp[:54]
    data = gojo_bmp[54:]

    message_in_binary = ''.join(format(ord(w), '08b') for w in message)

    byte_array_data = bytearray(data)

    index = 0

    for bit in message_in_binary:
        green_index = index * 3 + 1 # skip to green

        if bit == '1':
            byte_array_data[green_index] |= 1
        else:
            byte_array_data[green_index] &= ~1
        index += 1

        if index * 3 >= len(byte_array_data):
            print("| Finished encrypting data...")
            break

    print("| Writing data to encrypted gojo image...")

    with open("encryptedgojo.bmp", "wb") as gojo_encrypted_bmp:
        gojo_encrypted_bmp = gojo_encrypted_bmp.write(metadata + byte_array_data)
    
    print("| Done!")

    return message_length
    
    
        
        
    

def decrypter(message_length):
    #Cool aesthetics below
    print(decrypter_aesthetics)
    print("| Decrypting...                                                               |")

    data = gojo_encrypted_bmp[54:]
    decrypted_message_bin = ''

    byte_array_data = bytearray(data)

    print("| Looksmaxxing...")

    index = 0
    for bit in byte_array_data:
        green_index = index * 3 + 1 # skip to green

        bit = byte_array_data[green_index] &1
        decrypted_message_bin += str(bit)

        index += 1

        if index * 3 >= X * message_length:
            print("| Finished decrypting data...")
            break
    
    print("| Writing message...")
    
    message = ''.join([chr(int(decrypted_message_bin[i:i+8], 2)) for i in range(0, len(decrypted_message_bin), 8)])

    print(message)



    


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
        message_length_num = encrypter()
        message_length = str(message_length_num)
        print(line)
        with open("message_length.txt", "w") as message_length_file:
            message_length_update = message_length_file.write(message_length)
        break
    if action_response == "D":
        with open("message_length.txt", "r") as message_length_file:
            message_length_input = message_length_file.read()
        message_length_input_int = int(message_length_input)
        decrypter(message_length_input_int)
        print(line)
        break
    if action_response == "H":
        help_page()
    if action_response == "README":
        readme_file = open("readme.txt")
        readme = readme_file.read()
        print(readme)
    if action_response == "You are my special.":
        secret_file = open("aesthetics/secret.txt")
        secret = secret_file.read()
        print(secret)
    else:
        print("| Unknown command detected. Please try again!                                 |")
        print("| Type 'H' for help                                                           |")
        print(line)