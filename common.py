# write a function that checks if a string is a valid email

import re

def is_email(string):
    # Regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # If the string matches the regular expression, return True
    if re.fullmatch(regex, string):
        return True
    else:
        return False