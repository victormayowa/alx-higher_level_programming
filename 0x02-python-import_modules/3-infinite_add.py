#!/usr/bin/python3 
 if __name__ == "__main__":
     import sys

     argv = sys.argv[1:]
     total_sum = sum(int(arg) for arg in argv)

     print(total_sum)
