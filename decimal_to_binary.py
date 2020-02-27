#!/usr/bin/env python
"""decimal_to_binary.py

Convert a given 0 or greater integer to binary."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys

def main():
    try:
        dec = (int)(sys.argv[1])
        if (dec < 0):
            raise ValueError
    except(ValueError, IndexError):
        print("Usage: decimal_to_binary.py [n]")
        print("[n] = a decimal integer 0 or greater")
        sys.exit(1)

    loop_flag = True
    binary_digits = []

    while(loop_flag):
        binary_digits.append(dec % 2)
        if dec in [0, 1]:
            loop_flag = False
        else:
            dec = dec / 2

    binary_digits.reverse()
    binary = ""
    for digit in binary_digits:
        binary += "{}".format(digit)
    binary = (int)(binary)
    print(binary)

if __name__ == "__main__":
    main()
