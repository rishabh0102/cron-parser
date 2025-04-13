from src.fields.base import CronField

class DayOfMonthField(CronField):
    def __init__(self, field_str):
        super().__init__("day of month", field_str, 1, 31)