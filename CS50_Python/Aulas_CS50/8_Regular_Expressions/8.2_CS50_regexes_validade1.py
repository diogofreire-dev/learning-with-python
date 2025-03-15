import re

"""
.       any character except a newline

*       0 or more repetitions

+       1 or more repetitions

?       0 or 1 repetition

{m}     m repetitions

{m,n}   m to n repetitions

^       matches the start of the string

$       matches the end of the string 
        or just before the newline at 
        the end of the string

[]      set of characters

[^]     complementing the set

\d      decimal digit

\D      not a decimal digit

\s      whitwspace characters

\S      not a whitespace character

\w      word character ... as well as
        number and underscore _

\W      not a word character

A | B   either A or B

(...)   a group

(?:...) non-capturin version - "versão não capturável"
"""

email = input("What's your email? ").strip()

if re.search(r"^([^@]|\.)+@([^@]\.)?[^@]+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

"""
email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com$", email):
    print("Valid")
else:
    print("Invalid")
"""

"""
email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.com$", email):
    print("Valid")
else:
    print("Invalid")
"""