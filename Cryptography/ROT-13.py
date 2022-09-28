#Ceaser encryption ROT-13
#provides the set of letters
import string 

#User enters the password 
password = str(input("Enter password: "))
print("plain text :", password)
#The number for displacement for characters 
shift = 13

#Encryption 
alphabet =string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = password.translate(table)

print("encrypted text:", encrypted)