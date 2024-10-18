from CalculatorBase import Calculator


class divide(Calculator):
    def compute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero")
        return a / b