# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline().rstrip())
last=''
wins, max_wins, loses, max_loses = 0, 0, 0, 0
for i in range(n):
    wl = str(sys.stdin.readline().rstrip())
    if wl=='WIN':
        wins += 1
        loses = 0
        if wins > max_wins:
            max_wins = wins
        last = 'WIN'
    if wl=='LOSE':
        loses += 1 
        wins = 0
        if loses > max_loses:
            max_loses = loses
        last = 'LOSE'
    print(wins, loses, max_wins, max_loses)
