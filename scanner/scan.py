import nmap

def scan_even_ports(target):
    nm = nmap.PortScanner()

    even_ports = ','.join(str(port) for port in range(2, 65535) if port % 2 == 0)

    print(f"Scanning even-numbered ports on {target}...")
    
    nm.scan(target, even_ports)

    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    target_ip = input("Enter the IP address or hostname to scan: ")
    
    scan_even_ports(target_ip)