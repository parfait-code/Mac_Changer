# Mac_Changer -- MAC Address Changer Tool

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

- **If not installed** , install it using:

   ```bash
   sudo apt update
   sudo apt install python3

2. **Install net-tools:**
   The script relies on the ifconfig command, which is part of the net-tools package. Install it using:

   ```bash
   sudo apt install net-tools

3. **Download the Script:**
   Save the script to a file, e.g., mac_changer.py.

4. **Make the Script Executable:**
   Run the following command to make the script executable:

   ```bash
   chmod +x mac_changer.py
   ```

## Usage

**Command Syntax**

   ```bash
   sudo python3 mac_changer.py [options]
   ```
### Options

| Option                | Description                                      |
|:----------------------|:-------------------------------------------------|
| `-i`, `--interface`   | Specify the network interface (e.g., `eth0`).    |
| `-m`, `--mac`         | Specify the new MAC address.                     |
| `-r`, `--random`      | Generate a random MAC address.                   |
| `-ro`, `--restore`    | Restore the original MAC address.                |
| `-l`, `--list`        | List all available network interfaces.           |
| `-s`, `--status`      | Check the status of an interface (up/down).      |
| `-hn`, `--hostname`   | Spoof the system hostname.                       |
| `-info`               | Display the manual.                              |
| `-h`, `--help`        | Show the help menu.                              |

### **Examples**

1. **Change MAC Address:**

   ```bash 
   sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
   
2. **Generate Random MAC Address:**

   ```bash
   sudo python3 mac_changer.py -i eth0 -r

3. **Restore Original MAC Address:**

   ```bash
   sudo python3 mac_changer.py -i eth0 -ro

4. **List Available Interfaces:**

   ```bash
   sudo python3 mac_changer.py -l

5. **Check Interface Status:**

   ```bash
   sudo python3 mac_changer.py -s eth0

6. **Spoof Hostname:**

   ```bash
   sudo python3 mac_changer.py -hn newhostname

7. **Display Manual:**

   ```bash
   sudo python3 mac_changer.py -info

## Important Notes

- **Root Privileges:** This tool requires root privileges to change the MAC address.

- **Temporary Change:** The MAC address change is not persistent across reboots.

- **Legal Use:** Use this tool responsibly and only on networks you own or have permission to test on.

## License

This tool is open-source and distributed under the MIT License. Feel free to modify and distribute it as needed.

## Author

   **Name:** kouam parfait j

   **Contact:** kouamparfait5@gmail.com

   **GitHub:** [my github](https://github.com/parfait-code)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## Disclaimer

This tool is intended for educational and legitimate purposes only. Misuse of this tool, such as unauthorized access (without permission) to networks or illegal activities, is prohibited. The authors are not responsible for any misuse or damage caused by this tool.