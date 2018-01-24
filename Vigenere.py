def vigenere(message, key, decrypt = False):

    message = filter(str.isalpha, message).lower()
    key = filter(str.isalpha, key).lower()

    if not decrypt:
        print ("[Encrypting] ", message)
    else:
        print ("{Decrypting} ", message)

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    tonum = dict([(alpha[i], i) for i in range(len(alpha))])

    # Create Vigenere Square aka tabula recta
    lookup = dict([(a, 0) for a in alpha])
    for a in lookup:
        if not decrypt:
            lookup[a] = dict([(b, alpha[(tonum[a] + tonum[b]) % len(alpha)]) for b in alpha])
        else:
            lookup[a] = dict([(b, alpha[(tonum[a] - tonum[b]) % len(alpha)]) for b in alpha])

    out = ''
    for i in range(len(message)):
        letter = lookup[message[i].lower()][key[ i % len(key) ]]
        out += letter

    return out


key = input("Enter a secret Key")
msg = input("Enter a message")

print("1.Encrypt")
print("2.Decrypt")

ch = int(input("Do you want to Encrypt or Decrypt?"))
if ch==1:
     cipherText = vigenere(msg, key)
elif ch ==2:
    cipherText = ipu("enter a cipher text")
    plainText = vigenere(cipherText, key, True)


