#!/usr/bin/env python3

import os
import shutil
import sys
import socket
import psutil

def check_reboot():
    """Returns true if the computer has pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full (disk, min_gb, min_percent):
    """Returns true if there isnt enough disk space. False Otherwise"""
    du = shutil.disk_usage(disk)
    #calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full():
    """Returns true if the root partition is full, false otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_cpu_constrained():
    """Returns true if cpu is having too much usage, false otherwise"""
    return psutil.cpu_percent(1) > 75

def check_no_network():
    """Returns true if it fails to resolve Google's URL, false otherwise."""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def main():
    checks = [
        (check_reboot, "Pending reboot."),
        (check_root_full, "Root partition full."),
        (check_cpu_constrained, "CPU load too high."),
        (check_no_network, "No working network.")
    ]
    
    everything_ok = True
    
    for check, msg in checks:
        if check():
            print (msg)
            sys.exit(1)
            everything_ok = False
        if not everything_ok:
            sys.exit(1)
            
    print ("Everything ok.")
    sys.exit(0)
    
main()
