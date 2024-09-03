
## Nmap Port Scanner for Even-Numbered Ports

### Overview

This project is a port scanner that uses Nmap to scan even-numbered ports on a target host. The script takes an IP address or hostname as input and scans all even-numbered ports (2-65534) to identify open ports and their corresponding services.

### Prerequisites

- Python 3.x installed on your system.
- `python-nmap` Python library installed.
- Nmap tool installed on your system.

### Usage
- Step 1: Install Required Libraries
- Run pip install python-nmap to install the required Nmap library.
       ```python
         pip install python-nmap
         ```

- Step 2: Run Script
- Run the script and enter the IP address or hostname to scan when prompted.

### Output
The script will display the scan results, including:

- Host information (IP address and hostname)
- State of the host (up or down)
- Protocols used by the host (TCP, UDP, etc.)
- Open ports and their corresponding services
