from argparse import ArgumentParser
from src.cron_parser import CronParser
from src.logger import logger

PROGRAM_DESCRIPTION = """
This program takes a cron expression and breaks down each field to display the specific times it represents.
"""


def main():
    parser = ArgumentParser(description=PROGRAM_DESCRIPTION)
    parser.add_argument('cron_str', type=str, help='Cron expression to be parsed (must have 6 fields).')
    args = parser.parse_args()

    cron_parser = CronParser(args.cron_str)
    try:
        parsed_fields = cron_parser.parse()
        for name, item in parsed_fields.items():
            print(f"{name} {item}")

        logger.info("Cron parser executed !")

    except Exception as e:
        logger.error(f"failed to parse cron expression: {e}")


if __name__ == "__main__":
    main()