# PySyslog LFC

A lightweight, modular log processor with flow-based configuration.

## Features

- Flow-based log processing model
- Dynamic component loading
- Support for various input sources (Unix socket, file, flow chaining)
- Multiple parser types (RFC 3164, regex, passthrough)
- Flexible output options (file, TCP, memory for flow chaining)
- JSON-formatted logs
- Systemd service integration
- Clean, modern design without legacy syslog terminology

## Installation

### Quick Install (Using pip)

```bash
sudo pip3 install pysyslog-lfc
```

### Manual Installation

#### Prerequisites

- Python 3.8 or higher
- pip3
- git

#### Linux (Debian/Ubuntu)

1. Install system dependencies:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-dev git
```

2. Clone the repository:
```bash
git clone https://github.com/pysyslog/pysyslog-lfc.git
cd pysyslog-lfc
```

3. Install Python dependencies:
```bash
sudo pip3 install -r requirements.txt
```

4. Install the package:
```bash
sudo pip3 install .
```

5. Create configuration directories:
```bash
sudo mkdir -p /etc/pysyslog/conf.d
```

6. Copy configuration files:
```bash
sudo cp etc/pysyslog/main.ini /etc/pysyslog/
sudo cp etc/pysyslog/conf.d/*.ini /etc/pysyslog/conf.d/
```

7. Create system user:
```bash
sudo useradd -r -s /bin/false pysyslog
```

8. Set up systemd service:
```bash
sudo cp etc/systemd/system/pysyslog.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable pysyslog
sudo systemctl start pysyslog
```

#### Linux (RHEL/CentOS)

1. Install system dependencies:
```bash
sudo yum install python3 python3-pip python3-devel git
```

2. Clone the repository:
```bash
git clone https://github.com/pysyslog/pysyslog-lfc.git
cd pysyslog-lfc
```

3. Install Python dependencies:
```bash
sudo pip3 install -r requirements.txt
```

4. Install the package:
```bash
sudo pip3 install .
```

5. Create configuration directories:
```bash
sudo mkdir -p /etc/pysyslog/conf.d
```

6. Copy configuration files:
```bash
sudo cp etc/pysyslog/main.ini /etc/pysyslog/
sudo cp etc/pysyslog/conf.d/*.ini /etc/pysyslog/conf.d/
```

7. Create system user:
```bash
sudo useradd -r -s /sbin/nologin pysyslog
```

8. Set up systemd service:
```bash
sudo cp etc/systemd/system/pysyslog.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable pysyslog
sudo systemctl start pysyslog
```

#### macOS

1. Install system dependencies:
```bash
brew install python3 git
```

2. Clone the repository:
```bash
git clone https://github.com/pysyslog/pysyslog-lfc.git
cd pysyslog-lfc
```

3. Install Python dependencies:
```bash
pip3 install -r requirements.txt
```

4. Install the package:
```bash
pip3 install .
```

5. Create configuration directories:
```bash
sudo mkdir -p /etc/pysyslog/conf.d
```

6. Copy configuration files:
```bash
sudo cp etc/pysyslog/main.ini /etc/pysyslog/
sudo cp etc/pysyslog/conf.d/*.ini /etc/pysyslog/conf.d/
```

7. Set up launchd service:
```bash
sudo cp etc/launchd/com.pysyslog.plist /Library/LaunchDaemons/
sudo launchctl load /Library/LaunchDaemons/com.pysyslog.plist
```

#### Windows

1. Install Python 3.8 or higher from [python.org](https://www.python.org/downloads/)

2. Clone the repository:
```cmd
git clone https://github.com/pysyslog/pysyslog-lfc.git
cd pysyslog-lfc
```

3. Install Python dependencies:
```cmd
pip install -r requirements.txt
```

4. Install the package:
```cmd
pip install .
```

5. Create configuration directories:
```cmd
mkdir C:\ProgramData\pysyslog\conf.d
```

6. Copy configuration files:
```cmd
copy etc\pysyslog\main.ini C:\ProgramData\pysyslog\
copy etc\pysyslog\conf.d\*.ini C:\ProgramData\pysyslog\conf.d\
```

7. Install as Windows Service:
```cmd
python -m pysyslog install-service
```

## Configuration

For detailed configuration documentation, see:
- [Main Configuration](docs/configuration/main.md)
- [Flow Configuration](docs/configuration/flows.md)

## Usage

### Command Line

Start PySyslog LFC:
```bash
# Linux/macOS
sudo pysyslog

# Windows
pysyslog
```

### Service Management

#### Linux (systemd)
```bash
sudo systemctl start pysyslog
sudo systemctl stop pysyslog
sudo systemctl restart pysyslog
sudo systemctl status pysyslog
```

#### macOS (launchd)
```bash
sudo launchctl start com.pysyslog
sudo launchctl stop com.pysyslog
sudo launchctl unload /Library/LaunchDaemons/com.pysyslog.plist
sudo launchctl load /Library/LaunchDaemons/com.pysyslog.plist
```

#### Windows
```cmd
net start pysyslog
net stop pysyslog
```

### Viewing Logs

#### Linux
```bash
sudo journalctl -u pysyslog -f
```

#### macOS
```bash
sudo log show --predicate 'process == "pysyslog"' --last 5m
```

#### Windows
```cmd
Get-EventLog -LogName Application -Source pysyslog
```

## Development

### Project Structure

```
pysyslog-lfc/
├── bin/                    # Executable scripts
├── docs/                   # Documentation
│   └── configuration/      # Configuration docs
├── etc/                    # Configuration files
│   ├── pysyslog/
│   │   ├── main.ini
│   │   └── conf.d/
│   ├── systemd/           # Linux service files
│   ├── launchd/           # macOS service files
│   └── windows/           # Windows service files
├── lib/                    # Python package
│   └── pysyslog/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── flow.py
│       ├── components.py
│       ├── input/
│       ├── parser/
│       └── output/
└── setup.py
```

### Adding New Components

1. Create a new component file in the appropriate directory (`input/`, `parser/`, or `output/`)
2. Implement the required interface
3. Add the component to the `components` list in `main.ini`

## License

MIT License - see LICENSE file for details. 