import sys

address = sys.stdin.readline().split('.')
if len(address) == 4:
    print("IPv4")
else:
    print("IPv6")
