from src.fields.base import CronField

class MonthField(CronField):
    def __init__(self, field_str):
        super().__init__("month", field_str, 1, 12)