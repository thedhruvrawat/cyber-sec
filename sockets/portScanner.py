import nmap
from datetime import datetime

#Assigning local machine
ip = '127.0.0.1'
start = 700
end = 800

#Doing nmap scans on an IP without permission is illegal.

#Initializing a PortScanner object
scan = nmap.PortScanner()

time1 = datetime.now()
print("-"*60)
print("Scan started at ", time1)
print("-"*60)

for i in range(300, 400):
    port = scan.scan(ip, str(i))
    port = port['scan'][ip]['tcp'][i]['state']
    print(f"port{i} is {port}.")

time2 = datetime.now()
print("-"*60)
print("Scan ended at ", time2)
print("-"*60)

print(f"Time taken to scan {end-start} ports = {time2-time1}")
