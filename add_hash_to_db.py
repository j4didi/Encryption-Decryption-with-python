from functions import database_md5, hash_encryption

for word in range(1, 1000000):
    word = str(word)
    try:
        database_md5(word, hash_encryption(word))
        print(word)
    except Exception as e:
        print(e)
