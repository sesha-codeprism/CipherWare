import encrypt
import decrypt

create_arr = encrypt.create_array()
encrypt = encrypt.encrypt_array()
display = decrypt.print_array()
decrypt = decrypt.decrypt_array()

def print_menu():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Menu Option 3")




loop = True

while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = input("Enter your choice [1-3]: ")

    if choice == 1:
        plain_text = input("Enter a string")
        key = int(input("Enter a numerical key"))
        length = strlen(plain_text)
        create_arr(plain_text,length)
        encrypt(arr,key)
        display()
     elif choice == 2:
         cipher_text = input("Enter a string")
         key = int(input("Enter a numerical key"))
         length = strlen(cipher_text)
         create_arr(cipher_text,length)
         decrypt(arr,key)
         display(arr,length)

    elif choice == 3:
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")








