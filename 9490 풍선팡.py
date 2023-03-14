TC = int(input())
for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1,0,1,0]
    dc = [0,-1,0,1]

    maxV = 0
    for row in range(N):
        for col in range(M):
            sumV = arr[row][col]
            v = arr[row][col]
            for i in range(4):
                for j in range(1,v+1):
                    nr = row + dr[i]*j
                    nc = col + dc[i]*j
                    if 0<=nr<N and 0<=nc<M:
                        sumV += arr[nr][nc]
            if sumV > maxV:
                maxV = sumV

    print(f'#{tc} {maxV}')
