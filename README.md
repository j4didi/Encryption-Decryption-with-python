# Encryption-Decryption with Python

This repository contains a Python program for encryption and decryption using three different algorithms: MD5, DCL, and RSA. The program provides a simple interface for users to either encrypt or decrypt their data.

## Features

- **Encryption**: The program allows users to choose from three encryption algorithms:
  1. **MD5**: Encrypts the input text and returns the encrypted data. No additional parameters are required.
  2. **DCL (Dynamic Cipher Lock)**: This secure algorithm requires the user to:
      - Choose a key for encryption (any string).
      - Select an alpha code (a digit between 0-9).
      - Enter the data to be encrypted.
  3. **RSA**: The user needs to specify the key length (minimum 16) and then enter the data to be encrypted. The program then provides the encrypted data along with the public and private keys.

- **Decryption**: Users can decrypt data that was encrypted using the MD5 algorithm, given the following conditions:
  - The data is a number between 1 and 1,000,000, or
  - The data is a three-character alphanumeric combination.

## Repository Contents

- **`app.py`**: The main program file. Run this script to encrypt data or crack MD5-encrypted data (within the specified constraints).
- **`add_hash_to_db.py`**: This script adds numbers and their corresponding hashes to the database.
- **`data.db`**: The SQLite database file where hashed data is stored.
- **`dcl.py`**: Contains the implementation of the DCL encryption algorithm, which is invoked during the encryption process.
- **`functions.py`**: Includes utility functions used across the program for better organization and easier access. Functions are imported as needed in the `app.py` file.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/j4didi/Encryption-Decryption-with-python.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd Encryption-Decryption-with-python
   ```

3. Run the `app.py` script:
   ```bash
   python app.py
   ```

4. Follow the on-screen prompts to either encrypt or decrypt your data.

