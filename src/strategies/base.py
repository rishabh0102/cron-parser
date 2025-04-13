from abc import ABC, abstractmethod

class ExpandStrategy(ABC):
    @abstractmethod
    def expand(self, part, min_val, max_val):
        pass

    def validate(self, value, min_val, max_val):
        if not (min_val <= value <= max_val):
            raise ValueError(f"Value {value} out of range [{min_val}, {max_val}]")

