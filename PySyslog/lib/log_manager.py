import time
from datetime import datetime
from rate_limiter import RateLimiter
from patterns import parse_log_entry
from config_parser import load_config, load_included_configs, load_patterns

class LogManager:
    def __init__(self, config_path):
        self.config = load_config(config_path)
        self.config = load_included_configs(self.config, config_path)
        self.config = load_patterns(self.config, config_path)
        self.rate_limiter = RateLimiter(rate=self.config['global'].getint('log_rate_limit'))
        self.input_config = self.config['input=file']
        self.output_config = self.config['output=file']

    def read_logs(self):
        log_files = eval(self.input_config['log_files'])
        for file_path in log_files:
            with open(file_path, 'r') as f:
                for line in f:
                    if self.rate_limiter.allow():
                        yield line
                    else:
                        time.sleep(1)

    def process_logs(self):
        parser = self.input_config['parser']
        for log_entry in self.read_logs():
            parsed_entry = parse_log_entry(log_entry, parser)
            yield parsed_entry

    def write_logs(self):
        log_paths = eval(self.output_config['log_path'])
        for parsed_entry, log_path in zip(self.process_logs(), log_paths):
            with open(log_path, 'a') as f:
                f.write(f"{parsed_entry}\n")

    def rotate_logs(self):
        # Logic for rotating logs based on 'log_rotation' and 'archive_path' in config
        pass

    def run(self):
        self.write_logs()
        self.rotate_logs()
