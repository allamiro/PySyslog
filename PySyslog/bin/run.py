from log_manager import LogManager

def main():
    log_manager = LogManager('/path/to/pysyslog.conf')
    log_manager.run()

if __name__ == '__main__':
    main()
