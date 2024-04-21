# Assuming each pattern file defines a class with parse method
from . import cef_patterns, custom_patterns, json_patterns, syslog_patterns

def get_parser(parser_name):
    if parser_name == 'cef':
        return cef_patterns.CEFParser()
    elif parser_name == 'custom':
        return custom_patterns.CustomParser()
    elif parser_name == 'json':
        return json_patterns.JSONParser()
    elif parser_name == 'syslog':
        return syslog_patterns.SyslogParser()
    else:
        raise ValueError(f"Unknown parser: {parser_name}")

# Example parser class
class SyslogParser:
    def parse(self, log_entry):
        # Implement the parsing logic here
        return log_entry
