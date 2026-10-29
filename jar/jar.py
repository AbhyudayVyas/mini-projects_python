class Jar:
    def __init__(self, capacity=12, size = 0):
       self.capacity = capacity
       self.size = size
       if capacity<0:
           raise ValueError('too much cookie') 
    
    def __str__(self):
        n = self.size
        return str(n*'🍪')
    
    def deposit(self, n):
        if int(self.size+n) <= self.capacity:
            self.size+=n
        else:
            raise ValueError('too much cookie! won\'t fit in the jarr')
    
    def withdraw(self, n):
        if self.size-n >= 0:
            self.size = self.size-n
        else:
            raise ValueError(f'{n} number of cookies aren\'t even in the cookie jar u greedy fuck')
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            raise ValueError('cant be empty')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size<0:
            raise ValueError('cant be empty')
        self._size = size