from src.strategies.base import ExpandStrategy


class AsteriskStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        return set(range(min_val, max_val + 1))