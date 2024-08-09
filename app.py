from functions import *


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
        match get_user_item:
            case 1:
                while True:
                    get_algorithm = get_input_user(f'{encryption_items}Enter number of algorithm: ')
                    match get_algorithm:
                        case 1:
                            get_text = input("Enter the text you want to encrypt: \n")
                            result = hash_encryption(get_text)
                            print(f'Your hash: {result}')
                            try:
                                database_md5(get_text, result)
                                press_to_continue()
                            except Exception as e:
                                print(e)
                                press_to_continue()
                            break
                        case 2:
                            dcl_encryption()
                            break

                        case 3:
                            rsa_encryption()
                            press_to_continue()
                            break
                        case _:
                            print('Invalid number. try again.')
            case 2:
                while True:
                    get_algorithm = get_input_user(f'{encryption_items}Enter number of algorithm: ')
                    match get_algorithm:
                        case 1:
                            ctext = input('Enter the hash:')
                            ptext = get_ptext(ctext)

                            if ptext:
                                print(f'The plaintext is: {ptext}')
                                press_to_continue()
                            else:
                                print('Plaintext not found for the given MD5.')
                                press_to_continue()
                        case _:
                            print('We can only decrypt MD5 for now! please enter 1 :)')
                            press_to_continue()

            case 3:
                exit(0)

            case _:
                print('Invalid number! Please try again.')


main()