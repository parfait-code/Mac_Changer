# MAC Address Changer Tool

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

The **Mac_Changer** is a Python script designed to change the Media Access Control (MAC) address of a network interface on a Linux system. This tool is useful for testing, privacy protection, or troubleshooting network issues. It uses the `ifconfig` command to modify the MAC address temporarily.

---

## Features

- Change the MAC address of a specified network interface.
- Generate a random MAC address.
- Restore the original MAC address.
- List all available network interfaces.
- Check the status (up/down) of a network interface.
- Spoof the system hostname.
- Comprehensive manual with usage instructions.

---

## Requirements

- **Operating System:** Linux (tested on Ubuntu, Debian, and similar distributions).
- **Python Version:** Python 3.x.
- **Permissions:** Root privileges (required to change the MAC address).
- **Dependencies:** The `ifconfig` command must be installed (part of the `net-tools` package).

---

## Installation

1. **Install Python 3:**
   Ensure Python 3 is installed on your system. You can check by running:
   ```bash
   python3 --version