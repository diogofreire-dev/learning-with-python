class Jar:
    def __init__(self, capacity=10):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Cannot deposit more cookies than jar capacity allows")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")
        if n > self._size:
            raise ValueError("Cannot withdraw more cookies than are in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size