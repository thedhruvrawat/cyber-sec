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
            help = "Scan all ports (1-65535)", default=None
            )
    parser.add_option(
            '-s', '--specific', action="store", type="int", dest='spec',
            help = "Scan specific ports", default=None
            )
    parser.add_option(
            '-r', '--range', action="store", nargs=2, type="int", dest='range',
            help = "Scan ports in a specific range", default=None
            )
    (options, args) = parser.parse_args()
    if (options.com != None):
        print(f"Scanning common ports from 1 to 1024.")
        scanCommon()
        exit(0)
    if (options.all != None):
        print(f"Scanning all ports from 1 to 65535.")
        scanAll()
        exit(0)
    if (options.spec != None):
        print(f"Scanning port {options.spec}...")
        scanSpecific(options.spec)
        exit(0)
    if (options.range[0] != None):
        print(f"Scanning ports from Port #{options.range[0]} to Port #{options.range[1]}.")
        scanRange(options.range[0], options.range[1])
        exit(0)

def scanAll():
    start = 1
    end = 1024
    mainScanner(start, end+1)

def scanCommon():
    start = 1
    end = 65535
    mainScanner(start, end+1)

def scanSpecific(port):
    scan = nmap.PortScanner()
    check = scan.scan(ip, str(port))
    check = check['scan'][ip]['tcp'][port]['state']
    print(f"Port #{port} is {check}.")

def scanRange(beg, fin):
    mainScanner(beg, fin+1)

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
