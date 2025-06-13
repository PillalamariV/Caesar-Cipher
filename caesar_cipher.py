def encryption(message, shift):
    new_message = ""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    symbols = list("!@#$%^&*()1234567890")
    for x in message.lower():
        if (x != " " and not(x in symbols)):
            new_index = (alphabet.index(x) + shift) % 26
            new_message += alphabet[new_index]
        else:
            new_message += x
    print(new_message)

def decryption(message, shift):
    old_message = ""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    symbols = list("!@#$%^&*()1234567890")
    for x in message.lower():
        if (x != " " and not(x in symbols)):
            old_index = (alphabet.index(x) - shift) % 26
            old_message += alphabet[old_index]
        else:
            old_message += x
    print(old_message)

choice = input("Type 'encode' to encrypt, type'decode' to decrypt: ")
message = input("Type the message: ")
shift = int(input("Type shift number: "))
if (choice == "encode"):
    encryption(message, shift)
else:
    decryption(message, shift)
