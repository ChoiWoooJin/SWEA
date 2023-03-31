from collections import deque
r, c = list(map(int, input().split()))

arr = [list(input()) for _ in range(r)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

# print(arr)

def Q(ro,co):
    q = deque()
    lis = [(ro,co)]
    q.append((ro,co))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0<=nr<r and 0<=nc<c:
                if arr[nr][nc] != 'W':
                    q.append((nr,nc))
                    arr[nr][nc] = 'W'
                    lis.append((nr,nc))
    return lis

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            print(Q(i,j))
