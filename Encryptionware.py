import CC
import railfencecipher
import Playfair
import Vigenere

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())


def print_menu():
    print("Which Cipher do you want to use?")
    print("1. Caesar's Cipher")
    print("2. Playfair Cipher")
    print("3.Vigenere's cipher ")
    print("4.RailFence Cipher")
    print("5. Exit")
loop = True

while loop:
    print_menu()  # Displays menu
    choice = input("Enter your choice [1-5]: ")

    if choice == 1:
      run(CC.py)
    elif choice == 2:
      run(Playfair.py)
    elif choice == 3:
        run(Vigenere.py)
    elif choice == 4:
        run(railfencecipher.py)
    elif choice == 5:
        loop = False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
