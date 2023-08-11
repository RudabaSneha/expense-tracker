class Expense:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price
        
    def __repr__ (self):
        return f'<{self.name}, {self.type}, ${self.price:.2f}>'
    