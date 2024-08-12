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
                get_algorithm = get_input_user(f'{encryption_items}Enter number of algorithm: ')
                match_case_get_algorithm_case1(get_algorithm) #have a match case in function
            case 2:
                get_algorithm = get_input_user(f'{encryption_items}Enter number of algorithm: ')
                match_case_get_algorithm_case2(get_algorithm)
            case 3:
                exit(0)

            case _:
                print('Invalid number! Please try again.')


main()
