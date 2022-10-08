def solution(x):
    x = str(x)
    dividn = 0
    for i in x:
        dividn += int(i)

    if int(x) % dividn == 0:
        return True
    else:
        return False