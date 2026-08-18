import socket
import sys
from datetime import datetime

def scan_target(target_ip, ports):
    print("=" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Time Started: {str(datetime.now())}")
    print("=" * 50)

    try:
        for port in ports:
            # Create a TCP Socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0) # 1 second timeout
            
            # Attempt to connect to port
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting Script.")
        sys.exit()

    except socket.gaierror:
        print("\nHostname Could Not Be Resolved.")
        sys.exit()

    except socket.error:
        print("\nCould Not Connect to Server.")
        sys.exit()

if __name__ == "__main__":
    # Test target (Default: Localhost / Loopback)
    target = "127.0.0.1"
    
    # Common ports to scan (HTTP, HTTPS, FTP, SSH, Telnet)
    common_ports = [21, 22, 23, 80, 443, 8080]
    
    scan_target(target, common_ports)
