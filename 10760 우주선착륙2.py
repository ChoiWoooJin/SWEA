TC = int(input())
for tc in range(1, TC+1):

    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,-1,-1,-1,0,1,1,1]

    lis = []
    for row in range(N):
        for col in range(M):
            cnt = 0
            for i in range(8):
                newR = row+dr[i]
                newC = col+dc[i]
                if newR>=0 and newR <= N-1 and newC >= 0 and newC <= M-1:

                    if arr[newR][newC] < arr[row][col]:
                        cnt += 1
            lis.append(cnt)

    cnt2 = 0
    for l in lis:
        if l >= 4:
            cnt2 += 1

    print(f'#{tc} {cnt2}')







