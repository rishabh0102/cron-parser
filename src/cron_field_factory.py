from src.fields import (
    MinuteField,
    HourField,
    DayOfMonthField,
    MonthField,
    DayOfWeekField,
    CommandField
)


class CronFieldFactory:
    _field_classes = {
        "minute": MinuteField,
        "hour": HourField,
        "day of month": DayOfMonthField,
        "month": MonthField,
        "day of week": DayOfWeekField,
        "command": CommandField,
    }

    @staticmethod
    def create_field(name, field_str):
        field_class = CronFieldFactory._field_classes.get(name)
        if not field_class:
            raise ValueError(f"Unknown field name: {name}")
        return field_class(field_str)