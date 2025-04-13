from src.fields.base import CronField

class MinuteField(CronField):
    def __init__(self, field_str):
        super().__init__("minute", field_str, 0, 59)