class StringFOO:
    def __init__(self):
        self.name = 'Louis'

    def set_string(self, name):
        self.name = name

    def print_string(self):
        print(self.name.upper())

foo = StringFOO()
foo.print_string()