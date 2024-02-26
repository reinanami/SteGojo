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
with open("gojo.bmp", "rb") as gojo_bmp_file: #Reading the original image. This image of Gojo is from MAPPA Studio, character is by Mangaka, Gege.
    gojo_bmp = gojo_bmp_file.read() #It reads the bmp globally

with open("encryptedgojo.bmp", "rb") as gojo_encrypted_bmp: #For the encrypted image
    gojo_encrypted_bmp = gojo_encrypted_bmp.read() #It reads the bmp globally


def encrypter():
    #Formatting the cool aesthetics below
    print(encrypter_aesthetics)

    num_of_messages = int(input("How many messages would you like to encrypt?: ")) #Asks for the amount of messages the user would want to input
    message_list = [] #Empty list for tracking the messages
    message_length_list  = [] #Empty list for tracking the message length

    with open("num_of_messages.txt", "w") as num_of_messages_tracker:
        num_of_messages_tracker.write(str(num_of_messages))
    
    metadata = gojo_bmp[:54] #We want to save the metadata so that it saves the bmp file properly
    data = gojo_bmp[54:] #We want to split it so that data can be encrypted without complications
    byte_array_data = bytearray(data) #We use bytearray so it formats into data[X][Y][ColorPixel]

    for num in range(num_of_messages): #This function ensures that the amount of message encrypted is appropriate
        message = input("| enter message " + str(num + 1) + " :")
        message_list.append(message)
        num += 1

    index = 0 #Index is initialized to 0

    for message in message_list: 
        
        message_length = len(message) #First we remember the length of our message for later

        message_in_binary = ''.join(format(ord(l), '08b') for l in message) #We turn the letters 'l' within the message into 08b format as 1 letter = 8 bits = 1 byte


        for bit in message_in_binary: #For every bit inside the message
            green_index = index * 3 + 1 # We skip to green. 3 serves as an offset

            if bit == '1': #If it matches as one
                byte_array_data[green_index] |= 1 #Bitwise OR 1
            else: #Otherwise
                byte_array_data[green_index] &= ~1 #Bitwise AND not 1 (0)
            
            index += 1 # We increment the index here
            
            print("| " + str(index) + " bits out of " + str(message_length * 8) + " done...") #Bit counter for fun

            if index * 3 >= len(byte_array_data):
                print("| Finished encrypting data...") #Ensure that there are no index errors
                break
            
        message_length_list.append(message_length) #Append message length 

        print("| Writing data to encrypted gojo image...")

        with open("encryptedgojo.bmp", "wb") as gojo_encrypted_bmp:
            gojo_encrypted_bmp = gojo_encrypted_bmp.write(metadata + byte_array_data) #We write the encrypted bmp onto encrypted gojo bmp

    print("| Done!")

    return message_length_list #Return the message length so that it remembers how to decrypt the message properly 
    

def decrypter(message_length_input_list, num_of_messages):
    print("| You have " + str(num_of_messages) + " messages to decrypt.")
    amt_decrypt = int(input("How many messages would you like to decrypt?: "))
    if amt_decrypt > int(num_of_messages):
        print("|ERROR! Please enter a number less than " + str(num_of_messages)) #Error in case someone enters more than the maximum messages from the encryption
        return 

    #Cool aesthetics below
    print(decrypter_aesthetics)

    data = gojo_encrypted_bmp[54:] #Split the data from the metadata
    byte_array_data = bytearray(data)
    index = 0 #initialize index

    for amt in range(amt_decrypt):
        print("| Decrypting " + str(amt + 1) + "...") #We decrypt one by one
        message_length = message_length_input_list[amt]
        decrypted_message_bin = ''

        for _ in range(message_length * 8):
            green_index = index * 3 + 1 # skip to green
            bit = byte_array_data[green_index] &1 #Isolate the LSB of the byte
            decrypted_message_bin += str(bit) #Add the bit onto the message string
            index += 1
    
        print("| Writing message...")

        message = ""
        for c in range(0, len(decrypted_message_bin), 8):
            byte = decrypted_message_bin[c :c+8] #Using base2 binary, we sort the binary numbers into 8 bits so that it can be converted into a character
            message += chr(int(byte, 2))

        return message

#main
print(title)
while True:
    print(main_aesthetics)
    action_response = input("| Your response: ")
    print(line)
    if action_response == "E":
        message_length_num = encrypter()
        print(line)
        with open("message_length.txt", "w") as message_length_file:
            message_length_str = ','.join(map(str, message_length_num))
            message_length_file.write(message_length_str) #We want to secure the message length
        break
    if action_response == "D":
        with open("message_length.txt", "r") as message_length_file:
            message_length_input_str = message_length_file.read() #We want to read the message length so that we decrypt the right size
            message_length_input_list = [int(i) for i in message_length_input_str.split(',')]
        with open("num_of_messages.txt", "r") as num_of_messages_tracker:
            num_of_messages = num_of_messages_tracker.read()
        decrypted_message = decrypter(message_length_input_list, num_of_messages)
        print("| " + decrypted_message)
        print(line)
        break
    if action_response == "README":
        readme_file = open("readme.txt") #Readme to document commands and important information
        readme = readme_file.read()
        print(readme)
    else:
        print("| Unknown command detected. Please try again!                                 |") #This code constitutes an error due to an unknown command
        print(line)
