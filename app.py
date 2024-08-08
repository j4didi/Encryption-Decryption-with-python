from functions import *
import sqlite3


show_list_items = """1-Encryption
2-Decryption
3-Exit
"""

encryption_items = """Which algorithm would you like to use?
1-MD5 hash
2-DCL
3-RSA
"""


decryption_items = """Which algorithm would you like to decrypt?
1-MD5 hash"""

def main():
    while True:
        get_user_item = get_input_user(f'{show_list_items}Enter number of your choice: ')
        if get_user_item == 1:
            while True:
                get_algorithm = get_input_user(f'{encryption_items}Enter number of algorithm: ')

                if get_algorithm == 1:
                    get_text = input("Enter the text you want to encrypt: \n")
                    result = hash_encryption(get_text)
                    print(f'Your hash: {result}')
                    database_md5(get_text, result)
                    press_to_continue()
                    break

                elif get_algorithm == 2:
                    dcl_encryption()
                    break

                elif get_algorithm == 3:
                    rsa_encryption()
                    press_to_continue()
                    break
                else:
                    print('Invalid number. try again.')
        elif get_user_item == 2:
            while True:
                get_algorithm = get_input_user(f'{encryption_items}Enter number of algorithm: ')
                if get_algorithm == 1:
                    ctext = 'example_ciphertext'
                    ptext = get_ptext(ctext)

                    if ptext:
                        print(f'The corresponding plaintext is: {ptext}')
                    else:
                        print('Plaintext not found for the given ciphertext.')
        elif get_user_item == 3:
            exit(0)
        else:
            print('Invalid number! Please try again.')


main()