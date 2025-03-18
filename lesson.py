letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def decrypt(cypher, key):
    """
    Summary: Takes in an encrypted message and decrypts it by a known key.

    Inputs:
      - cypher (str): The message to be decrypted.
      - key (int): The offset that the message should be decrypted by.

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
    print("Offset: " + str(i))
    return decrypt(message, i)


def main():
    while True:
        try:
            mode = input("Would you like to encrypt or decrypt a message? ")
            if mode.lower() == "encrypt":
                message = input("What is the message you want to encrypt? Or press 0 to end. ")
                if message == "0":
                    break
                offset = int(input("What is the offset? "))

                encryptedmessage = encrypt(message, offset)
                print(encryptedmessage)

            if mode.lower() == "decrypt":
                cypher = input("What is the cypher you want to decrypt? Or press 'E' to end. ")
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