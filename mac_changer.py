import subprocess
import re
import random
import argparse
import logging
from colorama import Fore, Style

# Banner
BANNER = f"""
{Fore.GREEN}╔══════════════════════════════════════════════════════════════╗
║              
║               MACShadow - Change MAC Address                 ║ 
║                                                              ║
║              Author: Kouam Parfait Junior                    ║
║              Version: 2.0                                    ║
║              GitHub: Danielhttps://github.com/parfait-code   ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

# Manual (Info Command)
MANUAL = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                      MACShadow Manual                        ║
╠══════════════════════════════════════════════════════════════╣
║ {Fore.YELLOW}Description:{Fore.CYAN}                                                 ║
║ This tool allows you to change the MAC address of a network  ║
║ interface on a Linux system. It is useful for testing,       ║
║ privacy protection, or troubleshooting network issues.       ║
║                                                              ║
║ {Fore.YELLOW}Usage:{Fore.CYAN}                                                       ║
║ sudo python3 mac_changer.py [options]                        ║
║                                                              ║
║ {Fore.YELLOW}Options:{Fore.CYAN}                                                     ║
║ -i, --interface    Specify the network interface             ║
║ -m, --mac         Specify the new MAC address                ║
║ -r, --random      Generate a random MAC address              ║
║ -ro, --restore    Restore the original MAC address           ║
║ -l, --list        List all available network interfaces      ║
║ -s, --status      Check the status of an interface (up/down) ║
║ -hn, --hostname   Spoof the system hostname                  ║
║ -info             Display this manual                        ║
║ -h, --help        Show the help menu                         ║
║                                                              ║
║ {Fore.YELLOW}Examples:{Fore.CYAN}                                                    ║
║ 1. Change MAC address:                                       ║
║    sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55  ║
║ 2. Generate a random MAC address:                            ║
║    sudo python3 mac_changer.py -i eth0 -r                    ║
║ 3. Restore original MAC address:                             ║
║    sudo python3 mac_changer.py -i eth0 -ro                   ║
║ 4. List available interfaces:                                ║
║    sudo python3 mac_changer.py -l                            ║
║ 5. Check interface status:                                   ║
║    sudo python3 mac_changer.py -s eth0                       ║
║ 6. Spoof hostname:                                           ║
║    sudo python3 mac_changer.py -hn newhostname               ║
║ 7. Display manual:                                           ║
║    sudo python3 mac_changer.py -info                         ║
║                                                              ║
║ {Fore.YELLOW}Important Notes:{Fore.CYAN}                                             ║
║ - This tool requires root privileges.                        ║
║ - MAC address changes are temporary (not persistent).        ║
║ - Use responsibly and only on networks you own or have       ║
║   permission to test on.                                     ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

# Logging setup
logging.basicConfig(filename="mac_changer.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Store original MAC address
ORIGINAL_MAC = {}

def generate_random_mac():
    """Generate a random MAC address."""
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    return ":".join(f"{x:02x}" for x in mac)

def is_valid_mac(mac):
    """Validate the MAC address format."""
    return re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac) is not None

def get_current_mac(interface):
    """Retrieve the current MAC address of the specified interface."""
    try:
        output = subprocess.check_output(["ifconfig", interface])
        mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", output.decode())
        return mac_address_search_result.group(0) if mac_address_search_result else None
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[-] Could not get MAC address for interface {interface}.{Style.RESET_ALL}")
        return None

def change_mac(interface, new_mac):
    """Change the MAC address of the specified interface."""
    print(f"{Fore.YELLOW}[+] Changing MAC address for {interface} to {new_mac}{Style.RESET_ALL}")
    try:
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["sudo", "ifconfig", interface, "up"])
        current_mac = get_current_mac(interface)
        if current_mac == new_mac:
            print(f"{Fore.GREEN}[+] MAC address was successfully changed to {current_mac}{Style.RESET_ALL}")
            logging.info(f"Interface: {interface}, New MAC: {current_mac}")
        else:
            print(f"{Fore.RED}[-] MAC address did not get changed.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

def restore_original_mac(interface):
    """Restore the original MAC address of the specified interface."""
    if interface in ORIGINAL_MAC:
        original_mac = ORIGINAL_MAC[interface]
        print(f"{Fore.YELLOW}[+] Restoring original MAC address for {interface} to {original_mac}{Style.RESET_ALL}")
        change_mac(interface, original_mac)
    else:
        print(f"{Fore.RED}[-] No original MAC address found for {interface}.{Style.RESET_ALL}")

def list_interfaces():
    """List all available network interfaces."""
    try:
        output = subprocess.check_output(["ifconfig", "-a"])
        interfaces = re.findall(r"^(\w+):", output.decode(), re.MULTILINE)
        print(f"{Fore.CYAN}[+] Available interfaces:{Style.RESET_ALL}")
        for interface in interfaces:
            print(f" - {interface}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[-] Could not list interfaces.{Style.RESET_ALL}")

def get_interface_status(interface):
    """Check the status (up/down) of the specified interface."""
    try:
        output = subprocess.check_output(["ifconfig", interface])
        return "UP" if "UP" in output.decode() else "DOWN"
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[-] Could not get status for interface {interface}.{Style.RESET_ALL}")
        return None

def spoof_hostname(new_hostname):
    """Spoof the system hostname."""
    try:
        subprocess.call(["sudo", "hostnamectl", "set-hostname", new_hostname])
        print(f"{Fore.GREEN}[+] Hostname changed to {new_hostname}{Style.RESET_ALL}")
        logging.info(f"Hostname changed to {new_hostname}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

def display_manual():
    """Display the manual."""
    
    print(MANUAL)

def main():
    parser = argparse.ArgumentParser(description="MAC Address Changer", add_help=False)
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    parser.add_argument("-r", "--random", action="store_true", dest="random", help="Generate a random MAC address")
    parser.add_argument("-ro", "--restore", action="store_true", dest="restore", help="Restore original MAC address")
    parser.add_argument("-l", "--list", action="store_true", dest="list", help="List available interfaces")
    parser.add_argument("-s", "--status", dest="status", help="Check interface status (up/down)")
    parser.add_argument("-hn", "--hostname", dest="hostname", help="Spoof system hostname")
    parser.add_argument("-info", action="store_true", dest="info", help="Display the manual")
    parser.add_argument("-h", "--help", action="store_true", dest="help", help="Show help menu")
    args = parser.parse_args()

    if args.help:
        print(BANNER)
        parser.print_help()
        return

    if args.info:
        display_manual()
        return

    if args.list:
        list_interfaces()
        return

    if args.status:
        status = get_interface_status(args.status)
        if status:
            print(f"{Fore.CYAN}[+] Interface {args.status} is {status}{Style.RESET_ALL}")
        return

    if args.hostname:
        spoof_hostname(args.hostname)
        return

    if args.restore:
        if args.interface:
            restore_original_mac(args.interface)
        else:
            print(f"{Fore.RED}[-] Error: Please specify an interface to restore.{Style.RESET_ALL}")
        return

    if not args.interface:
        print(f"{Fore.RED}[-] Error: Please specify an interface.{Style.RESET_ALL}")
        return

    if args.random:
        args.new_mac = generate_random_mac()

    if not args.new_mac:
        print(f"{Fore.RED}[-] Error: Please specify a new MAC address or use --random.{Style.RESET_ALL}")
        return

    if not is_valid_mac(args.new_mac):
        print(f"{Fore.RED}[-] Error: Invalid MAC address format.{Style.RESET_ALL}")
        return

    print(BANNER)
    current_mac = get_current_mac(args.interface)
    if current_mac:
        ORIGINAL_MAC[args.interface] = current_mac
        print(f"{Fore.CYAN}[+] Current MAC address for {args.interface}: {current_mac}{Style.RESET_ALL}")
        change_mac(args.interface, args.new_mac)

if __name__ == "__main__":
    main()