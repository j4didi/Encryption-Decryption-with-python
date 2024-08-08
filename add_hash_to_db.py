from functions import database_md5, hash_encryption
import itertools

letters = '1234567890'

all_combinations = []
for r in range(3, 7):
    combinations = itertools.product(letters, repeat=r)
    all_combinations.extend([''.join(combination) for combination in combinations])

for word in all_combinations:
        database_md5(word,hash_encryption(word))
        print(word)