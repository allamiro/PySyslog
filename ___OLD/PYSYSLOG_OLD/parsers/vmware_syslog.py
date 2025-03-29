# Import Python libraries needed
import re

def vmware_syslog(log):
    cef_prefix = 'CEF:0|VM|VM|1.0||SYSLOG|Low|'  # << need to check the CEF guide for ArcSight
    log_patterns = [
        {
            'pattern': r"(\d+-\d+-\d+w+\d+:\d+.\d+\+\d+:\d+) (\d+.\d+.\d+.\d+)(.*)",
            'fields': ['timestamp', 'hostname', 'message'],
        }
    ]

    # This is where I match the CEF fields with the pattern extracted from above
    field_mapping = {
        'priority': 'cs1',
        'severity': 'sev',
        'timestamp': 'end',
        'hostname': 'dvchost',
    }

    for pattern_info in log_patterns:
        pattern = pattern_info['pattern']
        fields = pattern_info['fields']
        match = re.search(pattern, log)
        if match:  # Correctly indented now
            cef_values = ' '.join(
                f"{field_mapping[field]}={match.group(index)}"
                for index, field in enumerate(fields, start=1)
            )
            cef_log = f'{cef_prefix}{cef_values}'
            return cef_log

    return None
