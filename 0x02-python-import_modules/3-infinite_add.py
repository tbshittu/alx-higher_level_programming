#!/usr/bin/python3
import sys

def sum_arguments():
    if len(sys.argv) == 1:
        print("0")
    else:
        total = sum(int(arg) for arg in sys.argv[1:])
        print(total)

if __name__ == "__main__":
    sum_arguments()
