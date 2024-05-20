import random
import string

def generate_password(length, special_characters=True, numbers=True):

    ln = max(length, 8)
    letters = string.ascii_letters
    chars = string.punctuation
    number = string.digits
    
    has_number = False
    has_special = False
    if special_characters:
        letters += chars
    if numbers:
        letters += number
    # print(random.choice(letters))
    pwd= ""

    meets_criterion = False


    while not meets_criterion or len(pwd)<ln:
        current_char = random.choice(letters)
        pwd += random.choice(letters)
        
        if current_char in chars:
            has_special = True
            meets_criterion = True
        
        if current_char in number:
            has_number = True
            meets_criterion = True
        
        if special_characters and numbers:
            meets_criterion = has_number and has_special
    
    print(pwd)
    return pwd


generate_password(10, False, True )
