import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    Validates whether the input string is a valid IPv4 address.
    Returns True if valid, False otherwise.
    
    An IPv4 address must:
    - Have exactly 4 octets separated by periods
    - Each octet must be a number between 0 and 255, inclusive
    ---------------------------------------------------------------
    Versão em português:
    Valida se a string de entrada é um endereço IPv4 válido.
    Retorna True se for válido, False caso contrário.
    
    Um endereço IPv4 deve:
    - Ter exatamente 4 octetos separados por pontos
    - Cada octeto deve ser um número entre 0 e 255, inclusive
    """
    # Use regex to validate the IPv4 format
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)
    
    # If the pattern doesn't match, it's not a valid IPv4 address
    if not match:
        return False
    
    # Check that each octet is between 0 and 255
    for i in range(1, 5):
        octet = int(match.group(i))
        if octet < 0 or octet > 255:
            return False
    
    # If all checks pass, it's a valid IPv4 address
    return True


if __name__ == "__main__":
    main()