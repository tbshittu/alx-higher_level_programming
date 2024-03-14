#!/usr/bin/python3

if __name__ == "__main__":
import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1
    if num_arguments == 0:
        print("0 arguments.")
    else:
        print("{} argument:".format(num_arguments))
        for i in range(1, num_arguments + 1):
            print("{}: {}".format(i, sys.argv[i]))
