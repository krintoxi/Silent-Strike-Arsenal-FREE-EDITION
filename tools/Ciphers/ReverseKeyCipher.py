#KeyCipher
import pyperclip

#Input variable for the message
text = input("What is the Message to De-Cipher?: ")

#Message itself
message = (text)

#Tnhe Encryption/Decryption Key
key = 13

mode = 'decrypt' #Can be set to Encrypt or Decrypt

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

#stores the sting in the message
translated = ''

#Capitalize the string in the Message
message = message.upper()

#Run e/d code on every string in the message
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
                num = num - key
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        #Add Encrypted/Decrypted Numbers symbol at the end of translated
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
print('Output: ')        
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')        
print(translated)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
pyperclip.copy(translated)
