import subprocess
import socket

def get_ip_addresses():
    # Run 'arp -a' command to get the list of connected devices and their IPs
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    output = result.stdout
    ip_addresses = []
    
    # Extract IP addresses from arp output
    for line in output.splitlines():
        if "dynamic" in line:
            parts = line.split()
            if len(parts) > 1:
                ip_addresses.append(parts[0].strip('()'))  # Extract IP address

    return ip_addresses

def resolve_hostname(ip):
    try:
        # Use socket.gethostbyaddr to get hostname from IP
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        return None  # Couldn't resolve hostname

def get_connected_hosts():
    ip_addresses = get_ip_addresses()
    hosts = {}

    for ip in ip_addresses:
        print(f"Getting hostname of {ip}")
        hostname = resolve_hostname(ip)
        hosts[ip] = hostname if hostname else "Unknown Host"

    return hosts

# Example usage
if __name__ == "__main__":
    hosts = get_connected_hosts()
    for ip, hostname in hosts.items():
        print(f"IP: {ip} -> Hostname: {hostname}")
