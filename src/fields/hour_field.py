from src.fields.base import CronField

class HourField(CronField):
    def __init__(self, field_str):
        super().__init__("hour", field_str, 0, 23)