letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def decrypt(cypher, key):
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

def decrypt_unknown_key(message):
    for i in range(1, 26):
        print("Offset: " + str(i))
        print(decrypt(message, i))

message = "python is fun"
encryptedmessage = encrypt(message, 22)
decrypt_unknown_key(encryptedmessage)