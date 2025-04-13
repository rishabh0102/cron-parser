from src.fields.base import ParsableField

class CommandField(ParsableField):
    def __init__(self, command):
        self.command = command

    def parse(self):
        return self.command
