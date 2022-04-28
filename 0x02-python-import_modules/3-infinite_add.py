#!/usr/bin/python3
from sys import argv

total = 0
for num in range(1, len(argv)):
    num = int(argv[num])
    total += num
print("{}".format(total))

if __name__ == "__main__":
    argv
