# Network-Scanner
A Python-based network scanning tool that uses ARP requests to discover active devices on your local network.

## Description

This tool sends ARP (Address Resolution Protocol) requests to discover all active devices on a specified IP range or subnet. It displays the IP addresses and MAC addresses of all responding devices, making it useful for network administrators and security professionals to map their local network.

## Features

- Scans specified IP addresses or ranges using ARP protocol
- Displays IP addresses and corresponding MAC addresses
- Fast and efficient network device discovery
- Clean, formatted output for easy readability

## Requirements

- Python 3.x
- Scapy library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/network-scanner.git
cd network-scanner
```

2. Install the required dependencies:
```bash
pip install scapy
```

**Note:** On Linux systems, you may need to run the script with root privileges to send ARP packets.

## Usage

Run the scanner with the target IP address or range:

```bash
sudo python network_scanner.py -t <target>
```

### Examples

Scan a single IP:
```bash
sudo python network_scanner.py -t 192.168.1.1
```

Scan an IP range:
```bash
sudo python network_scanner.py -t 192.168.1.0/24
```

Scan a custom range:
```bash
sudo python network_scanner.py -t 10.0.0.1/16
```

### Options

- `-t`, `--target`: Target IP address or range (required)

## Sample Output

```
---------------------------------------------------------------
IP			MAC Address
---------------------------------------------------------------
192.168.1.1		00:11:22:33:44:55
192.168.1.5		AA:BB:CC:DD:EE:FF
192.168.1.10		12:34:56:78:90:AB
---------------------------------------------------------------
```

## How It Works

1. The script creates an ARP request packet for the specified target IP range
2. It broadcasts this request to all devices on the network
3. Devices respond with their IP and MAC addresses
4. The script collects and displays all responses in a formatted table

## Legal Disclaimer

This tool is intended for educational purposes and authorized network administration only. Only use this tool on networks you own or have explicit permission to scan. Unauthorized network scanning may be illegal in your jurisdiction.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## Author

Gilbert Baraka
