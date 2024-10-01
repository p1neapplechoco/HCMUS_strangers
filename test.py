import subprocess
import socket

class SIGMA:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.ip_addresses = []
        self.hosts = {}
        pass

    def get_connected_ip(self):
        output = subprocess.run(['arp', '-a'], capture_output=True, text=True).stdout
        output = output[output.find(self.ip):]

        for line in output.splitlines():
            if "dynamic" in line:
                parts = line.split()
                if len(parts) > 1:
                    self.ip_addresses.append(parts[0].strip('()'))
        
        return self.ip_addresses
        
    def get_connected_hosts(self):
        def get_host(ip):
            try:
                hostname, _, _ = socket.gethostbyaddr(ip)
                return hostname
            except socket.herror:
                return None
            
        for ip in self.ip_addresses:
            print(f"Getting hostname of {ip}")
            hostname = get_host(ip)
            if hostname:
                self.hosts[ip] = hostname

        return self.hosts
    

if __name__ == "__main__":
    this = SIGMA()
    this.get_connected_ip()
    this.get_connected_hosts()
    
    print(this.hosts)
    