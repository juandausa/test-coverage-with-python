class Calculator:
    # init method or constructor
    def __init__(self):
        return

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def pow(self, x, y):
        result = 1

        if y == 0:
            return result

        for i in range(y):
            result = self.multiply(result, x)

        return result

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by 0"
        return x * 1.0 / y
