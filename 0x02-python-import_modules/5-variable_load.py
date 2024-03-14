#!/usr/bin/python3
import importlib

def print_variable():
    variable_module = importlib.import_module("variable_load_5")
    print(variable_module.a)

if __name__ == "__main__":
    print_variable()
