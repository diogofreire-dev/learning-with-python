email = input("What's your email").strip()

username, domain = email.split("@")

if username and domain.endswitch(".com"):
    print("Valid")
else:
    print("Invalid")