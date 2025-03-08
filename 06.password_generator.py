import random
import string

def generator(min_len, include_number=True, include_spl_char=True):
    letters = string.ascii_letters
    number = string.digits
    spl_chr = string.punctuation

    # password strong check
    generate_passwd = random.choice(letters) + random.choice(number) + random.choice(spl_chr)
    print("Initial Password:" , generate_passwd)
    
    while len(generate_passwd) != min_len:
        generate_passwd +=  random.choice(letters) + random.choice(number) + random.choice(spl_chr)
    return generate_passwd





print("Final Password:",generator(3))