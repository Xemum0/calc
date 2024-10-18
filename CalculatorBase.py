from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def compute(self, a: float, b: float) -> float:
        pass