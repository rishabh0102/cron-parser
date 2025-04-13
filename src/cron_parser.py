from src.logger import logger
from src.cron_field_factory import CronFieldFactory


class CronParser:
    def __init__(self, cron_str):
        logger.debug(f"Initializing {self.__class__.__name__}, received cron_str: \"{cron_str}\"")
        fields = cron_str.split()
        if len(fields) < 6:
            error_msg = "Invalid cron string: expected at least 6 fields, got {}".format(len(fields))
            logger.error(error_msg)
            raise ValueError(error_msg)

        self.fields = {
            "minute": CronFieldFactory.create_field("minute", fields[0]),
            "hour": CronFieldFactory.create_field("hour", fields[1]),
            "day of month": CronFieldFactory.create_field("day of month", fields[2]),
            "month": CronFieldFactory.create_field("month", fields[3]),
            "day of week": CronFieldFactory.create_field("day of week", fields[4]),
            "command": CronFieldFactory.create_field("command", fields[5])
        }

    def parse(self):
        parsed_fields = {name: field.parse() for name, field in self.fields.items()}
        return parsed_fields

