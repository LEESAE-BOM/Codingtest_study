import sys

n = int(sys.stdin.readline())

menu = {1:"jjamppong", 2:"jjajangmyeon", 3:"bokkeumbap", 0:'jjajangmyeon'}

print(menu[n%4])