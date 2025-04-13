from src.strategies.base import ExpandStrategy


class RangeStepStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        range_part, step = part.split('/')
        step = int(step)
        self.validate(step, min_val, max_val)

        result = set()
        if range_part == "*":
            result.update(list(range(min_val, max_val + 1, step)))
        elif '-' in range_part:
            start, end = map(int, range_part.split('-'))
            self.validate(start, min_val, max_val)
            self.validate(end, min_val, max_val)
            result.update(list(range(start, end + 1, step)))
        else:
            start = int(range_part)
            self.validate(start, min_val, max_val)
            result.update(list(range(start, max_val + 1, step)))

        return result