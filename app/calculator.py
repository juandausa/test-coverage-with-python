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

    def pow(self, base, power):
        result = 1

        if power == 0:
            return result
        elif power > 0:
            for _ in range(power):
                result = self.multiply(result, base)
        else:
            for _ in range(abs(power)):
                result = self.divide(result, base)

        return result

    def divide(self, dividend, divisor):
        if divisor == 0:
            ValueError("Cannot divide by 0")
        return dividend * 1.0 / divisor
