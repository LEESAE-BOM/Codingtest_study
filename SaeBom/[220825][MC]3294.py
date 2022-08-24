n = int(input())

max_win = 0
max_lose = 0
win = 0
lose = 0

for i in range(n):
    if input() == 'WIN':
        win += 1
        lose = 0
    else:
        lose+=1
        win = 0
    if max_win<win:
        max_win = win
    elif max_lose <lose:
        max_lose = lose
    print(win,lose,max_win,max_lose)
