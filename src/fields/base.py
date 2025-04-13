from src.logger import logger
from src.strategies import (
    SingleValueStrategy,
    RangeStrategy,
    RangeStepStrategy,
    AsteriskStrategy
)

from abc import ABC, abstractmethod

class ParsableField(ABC):
    @abstractmethod
    def parse(self):
        pass

class CronField(ParsableField):
    def __init__(self, name, field_str, min_val, max_val):
        self.name = name
        self.field_str = field_str
        self.min_val = min_val
        self.max_val = max_val

    def parse(self):
        logger.debug(f"Parsing cron_field of type {self.name} with value: {self.field_str}")
        self.validate()
        parse_result = self.expand(self.field_str)
        logger.debug(f"Parsed cron_field of type {self.name} {self.field_str} to {parse_result}")
        return parse_result

    def validate(self):
        if not self.field_str:
            raise ValueError(f"{self.name} field is empty")

        # TODO: do a regex check
        logger.debug(f"{self.name} field is valid with value: {self.field_str}")


    def expand(self, field_str):
        result = set()
        parts = field_str.split(',')
        strategy_map = {
            '/': RangeStepStrategy,
            '-': RangeStrategy,
            '*': AsteriskStrategy,
        }

        for part in parts:
            logger.debug(f"Expanding part '{part}' for field '{self.name}'")
            part = part.lower()

            # Find the strategy based on the part's type
            strategy = None
            for key, strategy_class in strategy_map.items():
                if key in part:
                    strategy = strategy_class()
                    break
            if not strategy:
                strategy = SingleValueStrategy()

            result.update(strategy.expand(part, self.min_val, self.max_val))

        return sorted(result)