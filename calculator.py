class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b): #(failures=1)
        result = 0
        for _ in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = 0
        negative = (a < 0) ^ (b < 0)  # Determine if result should be negative
        a, b = abs(a), abs(b)

        while a >= b:
            a -= b  # Assuming `subtract` is implemented elsewhere
            result += 1

        return -result if negative else result
    
    def modulo(self, a, b):  # (failures=1)
        while a >= b:
            a = a - b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))