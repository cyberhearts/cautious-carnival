"""
Simple practice with random for generation password
"""
import string
import random

def generate_password(
            length: int = 16,
            use_uppercase: bool = True,
            use_numbers: bool = True,
            special: bool = False,
            bracket: bool = False
        ):
    """
    Func generate random password with needed params
    
    Params:

    length = len of password
    use_uppercase = pass will be contain UPPERCASE characters
    use_numbers = pass will be contain 0123456789
    special = pass will be contain !@#$%^&*,./~_+
    bracket = (){}[]
    """
    alphabet = string.ascii_lowercase
    if use_uppercase:
        alphabet += string.ascii_uppercase
    if use_numbers:
        alphabet += string.digits
    if special:
        alphabet += '!@#$%^&*,./~_+'
    if bracket:
        alphabet += '(){}[]'

    password = [random.choice(alphabet) for _ in range(length)]
    print(''.join(password))

if __name__ == "__main__":
    generate_password()
