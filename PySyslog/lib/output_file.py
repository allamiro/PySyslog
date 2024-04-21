class OutputFile:
    def __init__(self, log_paths):
        self.log_paths = log_paths

    def write_logs(self, parsed_entries):
        for parsed_entry, log_path in zip(parsed_entries, self.log_paths):
            with open(log_path, 'a') as file:
                file.write(f"{parsed_entry}\n")
