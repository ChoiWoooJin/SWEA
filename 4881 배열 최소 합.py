def per(k, sumV):
    global minV
    if sumV > minV:
        return

    if k == N:
        if minV > sumV:
            minV = sumV

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            per(k+1, sumV+ARR[i][k])
            visited[i] = False


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    minV = 101
    visited = [False] * N
    per(0,0)
    print(f'#{tc} {minV}')









