# 왜안됨

import sys

string = sys.stdin.readline().strip()
# string = list(sys.stdin.readline())

# for i in range(len(string)):
#     if string[i]=='\'':
#         string[i]="\\\'"
#     elif string[i]=='\"':
#         string[i]='\\\"'
#     elif string[i]=="\\":
#         string[i]="\\\\"

# string = ''.join(map(str, string))
# print(string)

print(string.translate(str.maketrans({'\\':'\\\\','\'':'\\\'','\"':'\\\"'})))