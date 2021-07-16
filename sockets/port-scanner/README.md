# Port Scanner 

A command-line based custom port-scanning tool built using [python-nmap](https://pypi.org/project/python-nmap/)

## Table of Contents

- [Installation](#installation)
- [Documentation](#documentation)
- [Working](#working)

## Installation

- Python version 3.6 or greater is required.
- Make sure you have `python-nmap` installed. It can be installed via `pip` command:

```bash
$ pip install python-nmap
```

## Documentation

```
$ python portScanner.py -h
Usage: portScanner.py [options]

Options:
  -h, --help           show this help message and exit
  -c, --common         Scan common ports (1-1024)
  -a, --all            Scan all ports (1-65535)
  -s SPEC, --specific=SPEC
                       Scan specific ports
  -r RANGE, --range=RANGE
                       Scan ports in a specific range
```

## Working

```
$ python portScanner.py -c
Scanning common ports from 1 to 1024.
------------------------------------------------------------
Scan started at  2021-07-16 23:07:24.693400
------------------------------------------------------------
Port #1 is closed.
Port #2 is closed.
Port #3 is closed.
...
Port #1022 is closed.
Port #1023 is closed.
Port #1024 is closed.
------------------------------------------------------------
Scan ended at  2021-07-16 23:07:27.666013
------------------------------------------------------------
Time taken to scan 1024 ports = 0:00:15.972613
```
```
$ python portScanner.py -a
Scanning common ports from 1 to 65535.
------------------------------------------------------------
Scan started at  2021-07-16 23:07:24.693400
------------------------------------------------------------
Port #1 is closed.
Port #2 is closed.
Port #3 is closed.
...
Port #65533 is closed.
Port #65534 is closed.
Port #65535 is closed.
------------------------------------------------------------
Scan ended at  2021-07-16 23:07:27.666013
------------------------------------------------------------
Time taken to scan 65535 ports = 0:00:02.972613
```
```
$ python portScanner.py -s 42069
Scanning port 42069...
Port #42069 is closed.
```
```
$ python portScanner.py -r 343 350
Scanning ports from Port #343 to Port #350.
------------------------------------------------------------
Scan started at  2021-07-16 23:12:23.752564
------------------------------------------------------------
Port #343 is closed.
Port #344 is closed.
Port #345 is closed.
Port #346 is closed.
Port #347 is closed.
Port #348 is closed.
Port #349 is closed.
Port #350 is closed.
------------------------------------------------------------
Scan ended at  2021-07-16 23:12:26.347593
------------------------------------------------------------
Time taken to scan 8 ports = 0:00:02.595029
```

> Doing nmap scans on an IP without permission is illegal. I have only used the localhost (127.0.0.1) in this example