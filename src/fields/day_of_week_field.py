from src.fields.base import CronField

class DayOfWeekField(CronField):
    MAP = {
        "sun": 1,
        "mon": 2,
        "tue": 3,
        "wed": 4,
        "thu": 5,
        "fri": 6,
        "sat": 7,
    }

    def __init__(self, field_str):
        super().__init__("day_of_week", field_str, 1, 7)
