#!/bin/python3

import sys
import socket
from datetime import datetime as dt

print("""

██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
╚██╗██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
 ╚███╔╝ ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
 ██╔██╗ ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██╔╝ ██╗███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                    
""")

#DEFINE OUR TARGET
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid Amount Of Arguments")
    print("Syntax: python3 scanner.py <ip>")

#ADD A BANNER
print("-" * 50)
print("Scanning target: "+target)
print("Time Started: "+str(dt.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is opened!")
        s.close()
        
except KeyboardInterrupt:
    print("\nEXITING PROGRAM")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
    
except socket.error:
    print("Could not connect to server")
    sys.exit()        