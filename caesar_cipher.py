print("\t\t\tWelcome to Caeser Cipher")

while (True):
    
    # print("Enter your choice :")
    print("1. For Encrypting")
    print("0. For Exit")
    
    a = int(input("Enter the choice : "))
    if (a == 1):
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter shift key (INTEGER):"))

        FIRST_UPPER_VALUE = ord("A")
        LAST_UPPER_VALUE = ord("Z")
        CHAR_RANGE = LAST_UPPER_VALUE - FIRST_UPPER_VALUE + 1

        def caesar_shift(message , shift):
            
            result = ""

            #Go through each letter in message
            for char in message.upper() :
                if char.isalpha():
                    char_code = ord(char)
                    new_char_code = char_code + shift
                    
                    if new_char_code > LAST_UPPER_VALUE :
                        new_char_code -= CHAR_RANGE
                        
                    if new_char_code < FIRST_UPPER_VALUE :
                        new_char_code += CHAR_RANGE
                        
                    new_char = chr(new_char_code)
                    result += new_char
                    
                else:
                    result += char


            print("INPUT VALUE: ", message)    
            print("OUTPUT VALUE:", result)
            
            
        caesar_shift(message , shift)  
        
    elif (a == 0 ):
        exit(0)
        
    else :
        print("Invalid choice.")
 
        