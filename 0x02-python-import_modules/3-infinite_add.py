#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv[1:]  # Exclude the script name from the arguments
    add = sum(int(arg) for arg in args)
    print(add)
