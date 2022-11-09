N = int(input())

for i in range(2**N):
    print(str(format(i, 'b')).zfill(N))