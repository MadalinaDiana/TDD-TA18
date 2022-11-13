class MiniCalculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def substract(self, reverse=False):
        if reverse:
            return self.b - self.a
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a // self.b
