from src.strategies.base import ExpandStrategy


class RangeStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        start, end = map(int, part.split('-'))
        self.validate(start, min_val, max_val)
        self.validate(end, min_val, max_val)
        return set(range(start, end + 1))