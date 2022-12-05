#!/usr/bin/env python3

### USAGE: Run this file and provide a log file as a command line arg.
### EX: ./filterLog.py fishy.log
### Enter what you are looking for when prompted

import sys
import os
import re

def error_search(log_file):
        error = input("What are you looking for? ")
        returned_errors = []
        with open(log_file, mode='r', encoding='UTF-8') as file:
                for log in file.readlines():
                        error_patterens = ["error"]
                        for i in range(len(error.split(' '))):
                                error_patterens.append(r'{}'.format(error.split(' ')[i].lower()))
                        if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterens):
                                returned_errors.append(log)
                file.close()
        return (returned_errors)

def file_output(returned_errors):
        with open(os.path.expanduser('~') + '/Desktop/errors_found.log', 'w') as file:
                for error in returned_errors:
                        file.write(error)
        file.close()

if __name__ == "__main__":
        log_file = sys.argv[1] 
        returned_errors = error_search(log_file)
        file_output(returned_errors)
        sys.exit(0)


#use with fishy.log
