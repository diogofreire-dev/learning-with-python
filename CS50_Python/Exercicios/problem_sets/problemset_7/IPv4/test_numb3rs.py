import sys
import os
# Adiciona o diretório atual ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from numb3rs import validate

def test_valid():
    """Test valid IPv4 addresses
    
    Testa endereços IPv4 válidos"""
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid():
    """Test invalid IPv4 addresses
    
    Testa endereços IPv4 inválidos"""
    assert validate("275.3.6.28") == False
    assert validate("cat") == False
    assert validate("192.168.1.256") == False