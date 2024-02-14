alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
            "u", "v", "w", "x", "y", "z"]

start = input("Type 'decrypt' to decode, 'encrypt' to encrypt: ").lower()
text = input("Enter text: ").lower()
shift = int(input("Enter shift: "))

def encrypt(text, shift):
    message = []
    for x in text:
        if x in alphabet:
            #range(inclusive, exclusive)
            for i in range(0, len(alphabet)):
                if (x == alphabet[i]):
                    #modulo has presedence (shift to right)
                    message.append(alphabet[(i + shift) % (len(alphabet))])
        else:
            message.append(x)
    encrypted = "".join(message)
    print(f"Encrypted Message: {encrypted}")
  
def decrypt(text, shift):
    message = []
    for x in text:
        if x in alphabet:
            for i in range(0, len(alphabet)):
                if (x == alphabet[i]):
                    #modulo by length of alphabet because otherwise at 25, z would be considered a since (25%25 = 0)
                    message.append(alphabet[(i - shift) % (len(alphabet))])

        else:
            message.append(x)
    decrypted = "".join(message)
    print(f"The message is: {decrypted}")

user = True
while (user):
    while start != "encrypt" and start != "decrypt":
        print("Please type exactly")
        start = input("Type 'decrypt' to decode, 'encrypt' to encrypt: ").lower()
    if start == "decrypt":
        decrypt(text, shift)
    elif start == "encrypt":
        encrypt(text, shift)
    cipher = input("\nType 'yes' if you want to go again, otherwise type 'no': ")
    if cipher == "no":
        user = False
    else:
        start = input("\nType 'decrypt' to decode, 'encrypt' to encrypt: ").lower()
        while start != "encrypt" and start != "decrypt":
            print("Please type exactly")
            start = input("Type 'decrypt' to decode, 'encrypt' to encrypt: ").lower()
        text = input("Enter text: ").lower()
        shift = int(input("Enter shift: "))

