from src.strategies.base import ExpandStrategy


class SingleValueStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        value = int(part)
        self.validate(value, min_val, max_val)
        return {value}