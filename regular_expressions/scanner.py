import re

# re.Scanner is an under-documented class in the re module
# and this is acknowledged by the core developers. See [1].
# But it is advised not to use this due to the lack of
# support and its immaurity. It is said [2] can bring
# [3] regex project into the standard library by Python 3.5.
# 1: http://bugs.python.org/issue5337
# 2: http://bugs.python.org/issue2636
# 3: https://pypi.python.org/pypi/regex

def get_tokens(input_text, scanner):
    """Returns a list of tokens found by a given scanner."""
    # A token returned from Scanner is always in a list
    token, remainder = scanner.scan(input_text)
    return token

def tk_PASSWORD(scanner, token):
    has_alpha = has_digit = False
    for char in token:
        if char.isalpha():
            has_alpha = True
        elif char.isdigit():
            has_digit = True

    if has_alpha and has_digit:
        return token
    else:
        raise Exception(
            "Password must contain a mixed of alphanumeric characters.")

pwd_scanner = re.Scanner([
    (r"\w{6,}", tk_PASSWORD),
    ])
