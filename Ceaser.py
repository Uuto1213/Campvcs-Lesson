key = int(input("key:"))
plaintext = input("plaintext:")
for char in plaintext:
    if char.isupper():
        print(chr((ord(char)+key-65)%26+65), end = "")
        
    elif char.islower():
        print(chr((ord(char)+key-97)%26+97), end = "")
        
    else:
        print(char,end = "")



