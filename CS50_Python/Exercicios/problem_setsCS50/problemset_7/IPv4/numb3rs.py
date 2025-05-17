import re

def main():
    """Main function to run when script is executed directly
    
    Função principal a ser executada quando o script é executado diretamente"""
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    """
    Validates if a string is a valid IPv4 address.
    
    A valid IPv4 address has 4 octets (0-255) separated by periods.
    
    Args:
        ip (str): The string to validate
        
    Returns:
        bool: True if valid IPv4 address, False otherwise
        
    Versão em português:
    Valida se uma string é um endereço IPv4 válido.
    
    Um endereço IPv4 válido tem 4 octetos (0-255) separados por pontos.
    
    Argumentos:
        ip (str): A string a ser validada
        
    Retorna:
        bool: True se for um endereço IPv4 válido, False caso contrário
    """
    try:
        # Use regex to match IPv4 format
        pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
        match = re.search(pattern, ip)
        
        # If pattern doesn't match, return False
        if not match:
            return False
        
        # Check that each octet is between 0 and 255
        for i in range(1, 5):
            octet = int(match.group(i))
            if octet < 0 or octet > 255:
                return False
        
        return True
    except:
        # If any error occurs (like conversion to int), it's not a valid IP
        return False

if __name__ == "__main__":
    main()