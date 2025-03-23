letters = 'abcdefghijklmnopqrstuvwxyz' # creates a string of letters the program can use to alter the message
num_letters = len(letters) # adds a variable equal to the of letters to allow offset to adjust for the ends of the letters list

def decrypt(cypher, key):
    """
    Summary: Takes in an encrypted message and decrypts it by a known key.

    Inputs:
      - cypher (str): The message to be decrypted.
      - key (int): An integer that is the offset that the message should be decrypted by.

    Outputs:
      - message (str): The decrypted message.

    """
    message = ''
    for character in cypher:
        if character in letters:
            char_index = letters.find(character)
            new_c = char_index + key
            if new_c >= num_letters:
                new_c -= num_letters
            message += letters[new_c]
        else:
            message += character
    return message

def encrypt(message, key):
    """
    Summary: Takes in a message and encrypts it by the desired key.

    Inputs:
      - message (str): The message to be encrypted.
      - key (int): An integer that is the offset that the message should be encrypted by.

    Outputs:
      - cypher (str): The encrypted message.
    """
    cypher = ''
    for character in message:
        if character in letters:
            char_index = letters.find(character)
            new_c = char_index - key
            if new_c >= num_letters:
                new_c -= num_letters
            cypher += letters[new_c]
        else:
            cypher += character
    return cypher

def decrypt_unknown_key(message, i):
    """
    Summary: Takes in an encrypted message and decrypts it when the key is unknown.

    Inputs:
      - message (str): The message to be decrypted.

    Outputs:
      - decrypt (str): The decrypted message for each possible key.
    """
    print("Offset: " + str(i))
    return decrypt(message, i)


def main():
    """
    Summary: Allows a user to input a message to encrypt or a cypher to decrypt. 
    
    Inputs:
      - User selects mode, 1 for encryption and 2 for decryption. Pressing 3 ends the program. 
      - If the user selects encryption, they are prompted to enter the message to encrypt and the key they want to offset by.
      - If the user selects decryption, they are prompted to enter the cypher and the key to decrypt by. If the key is unknown, they can type 0.

    Outputs:
      - If encryption is selected, the encrypted message will be returned. 
      - If decryption is selected and the key is known, the message will be returned.
      - If decryption is selected but the key is unknown, a string will return for every offset and the user can view them to find the message. 
    """
    while True:
        try:
            mode = int(input("Press 1 to encrypt a message, press 2 to decrypt a message, or press 3 to end. "))
            if mode == 3:
                break
            if mode == 1:
                message = input("What is the message you want to encrypt? Or press E to end. ").lower()
                if message.upper() == "E":
                    break
                offset = int(input("What is the offset? "))

                encryptedmessage = encrypt(message, offset)
                print(encryptedmessage)

            if mode == 2:
                cypher = input("What is the cypher you want to decrypt? Or press 'E' to end. ").lower()
                if cypher.upper() == "E":
                    break
                offset = int(input("Input the offset if you know it, if you don't know it, type '0'. "))
                if offset == 0:
                    for i in range(1, 26):
                        ans = decrypt_unknown_key(cypher, i)
                        print(ans)
                else:
                    ans = decrypt(cypher, offset)
                    print(ans)
                        
        except:
            print("Invalid inputs. Try again.")

# ===================================================================
if __name__ == "__main__":
    main()