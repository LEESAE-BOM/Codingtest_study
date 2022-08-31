from sys import stdin

input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs():
    check = set([start])
    q = deque([(start, 0)])
    while q:
        temp, cnt = q.popleft()  # 현재 문자열, 이동 횟수
        if temp == "1230":  # 타겟 문자열과 같으면 그 때의 이동 횟수 리턴
            return cnt

        idx = temp.index("0")  # 0인 곳의 인덱스
        r, c = idx // 2, idx % 2  # 이차원 맵 내 좌표로 변환
        for d in range(4):  # 4방향 중 위치 바꿀 수 있는 곳
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < 2 and 0 <= nc < 2):  # 범위 밖은 숫자 교환 불가
                continue

            nextTemp = list(temp)  # 위치 교환 쉽게 하기 위해 리스트로 변환
            nextIdx = nr * 2 + nc  # 위치 교환할 인덱스
            nextTemp[idx], nextTemp[nextIdx] = nextTemp[nextIdx], nextTemp[idx]
            nextTemp = ''.join(nextTemp)  # 문자열로 재변환

            if nextTemp in check:  # 이미 방문한 곳인지 확인
                continue
            check.add(nextTemp)  # 방문 표시
            q.append((nextTemp, cnt + 1))  # (위치 교환한 문자열, 횟수+1)해서 큐에 담기

    return -1  # 불가능한 경우


# main
start = ""  # 시작 문자열
for _ in range(2):
    start += ''.join(list(input().split()))
start= start.replace('X','0')
print(bfs())
