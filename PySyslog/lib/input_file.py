from patterns import get_parser

class InputFile:
    def __init__(self, log_files, parser_name):
        self.log_files = log_files
        self.parser = get_parser(parser_name)

    def read_logs(self):
        for file_path in self.log_files:
            with open(file_path, 'r') as file:
                for line in file:
                    yield self.parser.parse(line)
