TC = int(input())
for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))
    # arr 네 방향 0으로 패딩
    arr = [[0]*(N+2) for _ in range(N+2)]
    #[1] 초기돌 위치 놓기
    m = N // 2
    arr[m][m] = arr[m+1][m+1] = 2
    arr[m+1][m] = arr[m][m+1] = 1

    #[2] 흑돌 백돌 입력 받아서 처리
    for _ in range(M):
        si, sj, d = list(map(int, input().split()))
        arr[si][sj] = d
        #8방향 처리
        for di,dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            #해당 방향으로 뻗어 나가면서 처리
            tlst = []
            for mul in range(1, N):
                ni,nj = si+di*mul, sj+dj*mul
                if arr[ni][nj] == 0:  #빈칸 범위 밖이라 더이상 뻗어나갈 필요 없음
                    break
                elif arr[ni][nj] != d:
                    tlst.append((ni, nj))
                else:    #같은 돌이면 후보들을 뒤집고 종료
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = d
                    break

    bcnt = wcnt =0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')


##############################################################################
# i,j,검은
# for 8방향:
#     while 하얀색이 나올때까지:
#         ni,nj를 찾는다. (ni,nj 검은색)
#     if 찾았다면:
#         while ni,nj에서 i,j까지:
#             검은색으로 변경
