# Testes Unitários em Python

## Introdução aos Testes

Os testes unitários são essenciais para garantir que o código funcione corretamente.
Python tem duas bibliotecas principais para testes: `unittest` (padrão) e `pytest` (externa).

## Usando `unittest`

```python
# Ficheiro: calculadora.py
def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def divisão(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b
```

```python
# Ficheiro: test_calculadora.py
import unittest
from calculadora import soma, subtração, multiplicação, divisão

class TestCalculadora(unittest.TestCase):
    
    def test_soma(self):
        self.assertEqual(soma(5, 3), 8)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(-1, -1), -2)
    
    def test_subtração(self):
        self.assertEqual(subtração(5, 3), 2)
        self.assertEqual(subtração(3, 5), -2)
        self.assertEqual(subtração(-1, -1), 0)
    
    def test_multiplicação(self):
        self.assertEqual(multiplicação(5, 3), 15)
        self.assertEqual(multiplicação(-1, 3), -3)
        self.assertEqual(multiplicação(-1, -1), 1)
    
    def test_divisão(self):
        self.assertEqual(divisão(6, 3), 2)
        self.assertEqual(divisão(5, 2), 2.5)
        self.assertEqual(divisão(-6, 3), -2)
        
        # Testar exceção
        with self.assertRaises(ValueError):
            divisão(5, 0)

if __name__ == '__main__':
    unittest.main()
```

## Executar Testes

(Usando o terminal) Para executar os testes, podes:

1. Executar o ficheiro de teste diretamente:
```
python test_calculadora.py
```

2. Usar a linha de comandos:
```
python -m unittest test_calculadora.py
```

3. Descobrir e executar todos os testes:
```
python -m unittest discover
```

## Métodos de Asserção Comuns

```python
# Ficheiro: test_exemplo.py
import unittest

class TestExemplo(unittest.TestCase):
    
    def test_igualdade(self):
        self.assertEqual(5 + 5, 10)        # igual
        self.assertNotEqual(5 + 5, 11)     # diferente
    
    def test_booleanos(self):
        x = 10
        self.assertTrue(x > 5)             # verdadeiro
        self.assertFalse(x < 5)            # falso
    
    def test_identidade(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertIs(a, b)                # mesmo objeto
        self.assertIsNot(a, c)             # objetos diferentes
    
    def test_tipos(self):
        self.assertIsInstance("texto", str)  # verifica tipo
        self.assertIsNone(None)            # é None
    
    def test_comparações(self):
        self.assertGreater(10, 5)          # maior que
        self.assertLess(5, 10)             # menor que
        self.assertGreaterEqual(10, 10)    # maior ou igual
        self.assertLessEqual(5, 10)        # menor ou igual
    
    def test_containers(self):
        lista = [1, 2, 3]
        self.assertIn(2, lista)            # contém
        self.assertNotIn(5, lista)         # não contém
    
    def test_exceções(self):
        with self.assertRaises(ZeroDivisionError):
            x = 1 / 0
```

## Configuração e Limpeza

```python
import unittest
import os

class TestFicheiro(unittest.TestCase):
    
    def setUp(self):
        # Executa antes de cada teste
        self.nome_ficheiro = "teste_temp.txt"
        with open(self.nome_ficheiro, "w") as f:
            f.write("Dados de teste")
    
    def tearDown(self):
        # Executa depois de cada teste
        if os.path.exists(self.nome_ficheiro):
            os.remove(self.nome_ficheiro)
    
    def test_ler_ficheiro(self):
        with open(self.nome_ficheiro, "r") as f:
            dados = f.read()
        self.assertEqual(dados, "Dados de teste")
    
    def test_acrescentar_ficheiro(self):
        with open(self.nome_ficheiro, "a") as f:
            f.write(" adicionados")
        
        with open(self.nome_ficheiro, "r") as f:
            dados = f.read()
        
        self.assertEqual(dados, "Dados de teste adicionados")
```

## Dicas para Bons Testes

1. **Testes isolados**: cada teste deve testar apenas uma função ou método
2. **Nomes descritivos**: usar nomes que descrevam o que o teste verifica
3. **Testar casos limites**: valores zero, negativos, vazios, etc.
4. **Testar casos de erro**: verificar se as exceções são lançadas corretamente
5. **Pequenos e rápidos**: os testes devem executar rapidamente
6. **Independentes**: um teste não deve depender de outro
