import pytest
from jar import Jar

def test_init():
    # Testa se o jar é criado com capacidade padrão
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    
    # Testa capacidade personalizada
    jar = Jar(10)
    assert jar.capacity == 10
    
    # Testa erro com capacidade negativa
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    
    # Testa erro quando excede capacidade
    with pytest.raises(ValueError):
        jar.deposit(8)  # 5 + 8 = 13, mas capacidade é 12

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    
    # Testa erro quando tenta retirar mais do que tem
    with pytest.raises(ValueError):
        jar.withdraw(5)  # só tem 3 cookies