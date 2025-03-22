# Python Programação Orientada a Objetos

## Conceitos Básicos

A Programação Orientada a Objetos (OOP) é um paradigma que organiza o código em objetos, que são instâncias de classes.

```python
# Uma classe é como um modelo para criar objetos
class Pessoa:
    pass

# Criar um objeto (instância) da classe
pessoa1 = Pessoa()
pessoa2 = Pessoa()
```

## Classes e Objetos

```python
# Definir uma classe com atributos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criar objetos com diferentes valores
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Carlos", 30)

print(pessoa1.nome)  # "Ana"
print(pessoa2.idade)  # 30
```

## Métodos

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    # Método para apresentar a pessoa
    def apresentar(self):
        return f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos."
    
    # Método para fazer aniversário
    def fazer_aniversario(self):
        self.idade += 1

# Usar os métodos
pessoa = Pessoa("Maria", 22)
print(pessoa.apresentar())  # "Olá! Meu nome é Maria e tenho 22 anos."
pessoa.fazer_aniversario()
print(pessoa.idade)  # 23
```

## Atributos de Classe vs. Instância

```python
class Pessoa:
    # Atributo de classe (compartilhado por todas as instâncias)
    especie = "Humano"
    
    def __init__(self, nome, idade):
        # Atributos de instância (específicos para cada objeto)
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("João", 28)
pessoa2 = Pessoa("Maria", 22)

print(pessoa1.especie)  # "Humano"
print(pessoa2.especie)  # "Humano"

# Mudar um atributo de classe afeta todas as instâncias
Pessoa.especie = "Homo sapiens"
print(pessoa1.especie)  # "Homo sapiens"
print(pessoa2.especie)  # "Homo sapiens"
```

## Herança

```python
# Classe pai (superclasse)
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def fazer_som(self):
        print("Som genérico de animal")

# Classe filha (subclasse)
class Gato(Animal):
    def __init__(self, nome, raca):
        # Chama o construtor da classe pai
        super().__init__(nome, "Gato")
        self.raca = raca
    
    # Sobrescrevendo o método da classe pai
    def fazer_som(self):
        print("Miau!")

# Criar uma instância de Gato
meu_gato = Gato("Whiskers", "Siamês")
print(meu_gato.nome)    # "Whiskers"
print(meu_gato.especie)  # "Gato"
meu_gato.fazer_som()    # "Miau!"
```

## Encapsulamento

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        # Convenção: _ indica que deve ser tratado como privado
        self._saldo = saldo_inicial
    
    # Métodos para acessar e modificar o saldo
    def consultar_saldo(self):
        return self._saldo
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

# Usar a classe
conta = ContaBancaria("Ana", 1000)
conta.depositar(500)
print(conta.consultar_saldo())  # 1500
conta.sacar(200)
print(conta.consultar_saldo())  # 1300
```

## Overload de Operadores

```python
# Overload de operadores usando métodos especiais
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Representação como string
    def __str__(self):
        return f"Vetor({self.x}, {self.y})"
    
    # Operador +: soma de vetores
    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)
    
    # Operador -: subtração de vetores
    def __sub__(self, outro):
        return Vetor(self.x - outro.x, self.y - outro.y)
    
    # Operador *: produto escalar
    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Vetor(self.x * escalar, self.y * escalar)
        raise TypeError("Multiplicação apenas por números")
    
    # Operador ==: comparação de igualdade
    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y
    
    # Operador <: comparação (baseada na magnitude)
    def __lt__(self, outro):
        return self.magnitude() < outro.magnitude()
    
    # Método auxiliar
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5

# Usar o Overload de operadores
v1 = Vetor(3, 4)
v2 = Vetor(1, 2)

v3 = v1 + v2    # Usa __add__
print(v3)       # "Vetor(4, 6)"

v4 = v1 - v2    # Usa __sub__
print(v4)       # "Vetor(2, 2)"

v5 = v1 * 2     # Usa __mul__
print(v5)       # "Vetor(6, 8)"

print(v1 == v2) # Usa __eq__, False
print(v1 > v2)  # Usa __lt__, True (5 > √5)
```

## Métodos Dunder Comuns

```python
# Lista dos métodos dunder (double underscore) mais comuns:

# Básicos
__init__     # Construtor
__str__      # Representação como string informal (print)
__repr__     # Representação como string formal (para depuração)

# Operadores matemáticos
__add__      # +
__sub__      # -
__mul__      # *
__truediv__  # /
__floordiv__ # //
__mod__      # %
__pow__      # **

# Comparações
__eq__       # ==
__ne__       # !=
__lt__       # <
__gt__       # >
__le__       # <=
__ge__       # >=

# Comportamento de container
__len__      # len()
__getitem__  # obj[key]
__setitem__  # obj[key] = valor
__contains__ # in

# Outros
__call__     # obj()
```

## Exemplo: Classe Fração com Sobrecarga

```python
class Fracao:
    def __init__(self, numerador, denominador):
        self.num = numerador
        if denominador == 0:
            raise ValueError("Denominador não pode ser zero")
        self.den = denominador
        self._simplificar()
    
    def _mdc(self, a, b):
        # Algoritmo de Euclides para MDC
        while b:
            a, b = b, a % b
        return a
    
    def _simplificar(self):
        # Simplifica a fração
        mdc = self._mdc(abs(self.num), abs(self.den))
        self.num //= mdc
        self.den //= mdc
        # Garante que o denominador seja positivo
        if self.den < 0:
            self.num, self.den = -self.num, -self.den
    
    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"
    
    def __add__(self, outro):
        if isinstance(outro, int):
            outro = Fracao(outro, 1)
        novo_num = self.num * outro.den + outro.num * self.den
        novo_den = self.den * outro.den
        return Fracao(novo_num, novo_den)
    
    def __radd__(self, outro):
        # Para suportar: 5 + fracao
        return self.__add__(outro)
    
    def __sub__(self, outro):
        if isinstance(outro, int):
            outro = Fracao(outro, 1)
        novo_num = self.num * outro.den - outro.num * self.den
        novo_den = self.den * outro.den
        return Fracao(novo_num, novo_den)
    
    def __mul__(self, outro):
        if isinstance(outro, int):
            outro = Fracao(outro, 1)
        return Fracao(self.num * outro.num, self.den * outro.den)
    
    def __truediv__(self, outro):
        if isinstance(outro, int):
            outro = Fracao(outro, 1)
        return Fracao(self.num * outro.den, self.den * outro.num)
    
    def __eq__(self, outro):
        if isinstance(outro, int):
            outro = Fracao(outro, 1)
        return self.num == outro.num and self.den == outro.den

# Exemplo de uso
f1 = Fracao(1, 2)    # 1/2
f2 = Fracao(2, 3)    # 2/3

print(f1 + f2)       # 7/6
print(f1 - f2)       # -1/6
print(f1 * f2)       # 1/3
print(f1 / f2)       # 3/4
print(f1 + 2)        # 5/2
print(3 + f1)        # 7/2 (usando __radd__)
print(f1 == Fracao(2, 4))  # True (1/2 == 2/4 simplificado)
```

## Propriedades

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    # Getter
    @property
    def nome(self):
        return self._nome
    
    # Setter
    @nome.setter
    def nome(self, valor):
        if valor and isinstance(valor, str):
            self._nome = valor
        else:
            print("Nome inválido")
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if isinstance(valor, int) and 0 <= valor <= 120:
            self._idade = valor
        else:
            print("Idade inválida")

# Usar as propriedades
pessoa = Pessoa("João", 25)
print(pessoa.nome)  # "João"

pessoa.nome = "Carlos"  # Usa o setter
print(pessoa.nome)  # "Carlos"

pessoa.idade = 200  # Imprime "Idade inválida"
print(pessoa.idade)  # 25 (não mudou)
```

## Exemplo Prático: Sistema de Biblioteca

```python
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True
    
    def __str__(self):
        return f"{self.titulo} por {self.autor}"

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def emprestar_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn and livro.disponivel:
                livro.disponivel = False
                return f"{livro.titulo} emprestado com sucesso."
        return "Livro não disponível."
    
    def devolver_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn and not livro.disponivel:
                livro.disponivel = True
                return f"{livro.titulo} devolvido com sucesso."
        return "Erro na devolução."
    
    def listar_livros_disponiveis(self):
        return [livro for livro in self.livros if livro.disponivel]

# Exemplo de uso
minha_biblioteca = Biblioteca("Biblioteca Municipal")

livro1 = Livro("Dom Quixote", "Miguel de Cervantes", "123456")
livro2 = Livro("1984", "George Orwell", "789012")

minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)

print(minha_biblioteca.emprestar_livro("123456"))
print(len(minha_biblioteca.listar_livros_disponiveis()))  # 1
print(minha_biblioteca.devolver_livro("123456"))
print(len(minha_biblioteca.listar_livros_disponiveis()))  # 2
```
