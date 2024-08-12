import hashlib
import rsa
import sqlite3


def get_input_user(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Please enter a valid item number.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def rsa_key_len(key_len):
    while True:
        try:
            key_length = int(input(key_len))
            if key_length < 16:
                print("key length should be at least 16.")
                continue
            return key_length
        except ValueError:
            print("Invalid input. Please enter a numeric key length.")


def rsa_encryption():
    while True:
        try:
            key_length = rsa_key_len("Please enter a key length (at least 16): ")
            public_key, private_key = rsa.newkeys(key_length)
            message = input('Enter the text you want to encrypt: ')
            max_length = key_length // 8 - 11
            if len(message.encode()) > max_length:
                raise OverflowError(
                    f"Message is too long for the chosen key length. Maximum message length is {max_length} bytes.")
            enc_message = rsa.encrypt(message.encode(), public_key)
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")
        except OverflowError as oe:
            print(f"Error: {oe}. Please try again.")
    return print(f"Original: {message}\nEncrypted: {enc_message}\nPublic Key: {public_key}\nPrivate Key: {private_key}")


def match_case_get_algorithm_case1(get_algorithm): #For first match case
    match get_algorithm:
        case 1:
            get_text = input("Enter the text you want to encrypt: \n")
            result = hash_encryption(get_text)
            print(f'Your hash: {result}')
            press_to_continue()
        case 2:
            dcl_encryption()

        case 3:
            rsa_encryption()
            press_to_continue()
        case _:
            print('Invalid number. try again.')
def match_case_get_algorithm_case2(get_algorithm):
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


def get_alpha_user(prompt):
    while True:
        try:
            alpha = int(input(prompt))
            if alpha < 0 or alpha > 9:
                print("Alpha cannot be lower than 0 and bigger than 9")
                continue
            return alpha
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def hash_encryption(text):
    return hashlib.md5(text.encode()).hexdigest()


def dcl_encryption():
    from dcl import DCL
    key = input('Enter the key: \n')
    alpha = get_alpha_user('Enter the alpha between 0-9: \n')
    if alpha < 0 or alpha > 9:  # != 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        print('alpha must be between 0 and 9')
    plaintext = input("Enter the text you want to encrypt: \n")
    dcl_instance = DCL(key, alpha)
    result = dcl_instance.generate(plaintext)
    print(f'Your encrypted text with DCL algorithm: {result}')
    press_to_continue()


def database_md5(ptext, ctext):
    db = sqlite3.connect('data.db')
    cur = db.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS md5hash(
            plaintext TEXT PRIMARY KEY,
            ciphertext TEXT SECOND KEY
        )"""
    )

    cur.execute(
        """INSERT INTO md5hash(plaintext, ciphertext) VALUES(?, ?)""", (str(ptext), str(ctext))
    )
    db.commit()
    db.close()


def get_ptext(ctext):
    db = sqlite3.connect('data.db')
    cur = db.cursor()

    cur.execute("SELECT plaintext FROM md5hash WHERE ciphertext=?", (ctext,))
    result = cur.fetchone()

    db.close()

    if result:
        return result[0]
    else:
        return None


def press_to_continue():
    input('Press Enter to continue...')
