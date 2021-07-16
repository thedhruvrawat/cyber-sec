import nmap
import optparse
from datetime import datetime

ip = '127.0.0.1'
#Doing nmap scans on an ip without permission is illegal

def main():
    parser = optparse.OptionParser(usage="usage: %prog [options]")
    parser.add_option(
            '-c', '--common', action="store_true", dest='com',
            help = "Scan common ports (1-1024)", default=None
            )
    parser.add_option(
            '-a', '--all', action="store_true", dest='all',
            help = "Scan all ports (1-65536)", default=None
            )
    parser.add_option(
            '-s', '--specific', action="store", type="int", dest='spec',
            help = "Scan specific ports", default=None
            )
    (options, args) = parser.parse_args()
    if (options.com != None):
        scanAll()
        exit(0)
    if (options.all != None):
        scanCommon()
        exit(0)
    if (options.spec != None):
        print(f"Scanning port {options.spec}...")
        scanSpecific(options.spec)
        exit(0)

def scanAll():
    start = 11
    end = 20
    mainScanner(start, end)

def scanCommon():
    start = 1
    end = 10
    mainScanner(start, end)

def scanSpecific(port):
    scan = nmap.PortScanner()
    check = scan.scan(ip, str(port))
    check = check['scan'][ip]['tcp'][port]['state']
    print(f"Port #{port} is {check}.")

def mainScanner(start, end):
    #Initializing a PortScanner object
    scan = nmap.PortScanner()

    time1 = datetime.now()
    print("-"*60)
    print("Scan started at ", time1)
    print("-"*60)

    for i in range(start, end):
        port = scan.scan(ip, str(i))
        port = port['scan'][ip]['tcp'][i]['state']
        print(f"Port #{i} is {port}.")

    time2 = datetime.now()
    print("-"*60)
    print("Scan ended at ", time2)
    print("-"*60)

    print(f"Time taken to scan {end-start} ports = {time2-time1}")

if __name__ == "__main__":
    main() 
