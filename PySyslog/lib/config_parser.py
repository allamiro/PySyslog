import configparser
import glob

def load_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def load_included_configs(config, config_path):
    if 'include_configs' in config['global']:
        included_configs = glob.glob(config['global']['include_configs'])
        for path in included_configs:
            config.read(path)
    return config

def load_patterns(config, patterns_path):
    if 'include_patterns' in config['global']:
        pattern_files = glob.glob(config['global']['include_patterns'])
        patterns = {}
        for path in pattern_files:
            with open(path) as f:
                patterns[path] = f.read()
        config['patterns'] = patterns
    return config
