class Polybius:
    """A simple representation of the Polybius square."""

    def __init__(self, alpha='abcdefghiklmnopqrstuvwxyz', random=False, keyword=''):
        if random:
            from random import seed, randint
            self.alpha = ''
            seed()
            chars = [a for a in alpha]
            while len(chars) > 0:
                i = randint(0, len(chars) - 1)
                self.alpha += chars[i]
                del chars[i]
        else:
            self.alpha = ''
            keyword += alpha
            for a in keyword:
                if not a in self.alpha:
                    self.alpha += a
        from math import sqrt
        n = int(sqrt(len(alpha)))
        self.__square = [[self.alpha[i * n + j] for j in range(n)] for i in range(n)]
        self.__rev = dict(
            [(self.__square[i][j], (i, j)) for i in range(len(self.__square)) for j in range(len(self.__square))])

    def getletter(self, i, j):
        """Returns the letter in row i and column j."""
        return self.__square[i][j]

    def getposition(self, a):
        """Returns a tuple containing the numbers for the row and column a is in."""
        return self.__rev[a]


def playfair(message, key, decrypt=False):
    if isinstance(key, str):
        key = Polybius(keyword=key)
    elif not isinstance(key, Polybius):
        raise Exception("Invalid key")

    message = filter(lambda n: n in key.alpha, message)
    message = [a for a in message]
    out = ''

    from math import sqrt
    n = int(sqrt(len(key.alpha)))

    for i in range(0, len(message), 2):
        if i + 1 == len(message):
            message.append('x')
        if message[i] == message[i + 1]:
            message.insert(i + 1, 'x' if message[i] != 'x' else 'q')

        row1, col1 = key.getposition(message[i])
        row2, col2 = key.getposition(message[i + 1])

        if col1 == col2:
            if decrypt:
                out += key.getletter((row1 - 1) % n, col1)
                out += key.getletter((row2 - 1) % n, col2)
            else:
                out += key.getletter((row1 + 1) % n, col1)
                out += key.getletter((row2 + 1) % n, col2)
        elif row1 == row2:
            if decrypt:
                out += key.getletter(row1, (col1 - 1) % n)
                out += key.getletter(row2, (col2 - 1) % n)
            else:
                out += key.getletter(row1, (col1 + 1) % n)
                out += key.getletter(row2, (col2 + 1) % n)
        else:
            out += key.getletter(row1, col2) + key.getletter(row2, col1)

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
