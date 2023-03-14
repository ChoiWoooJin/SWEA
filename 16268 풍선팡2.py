# 1. 패딩
#
# TC = int(input())
# for tc in range(1, TC+1):
#
#     N ,M = list(map(int, input().split()))
#     arr = [[0] * (M + 2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]
#
#
#
#     lis = []
#     for i in range(1,N+1):
#         for j in range(1,M+1):
#             lis.append(arr[i][j]+arr[i-1][j]+arr[i][j-1]+arr[i+1][j]+arr[i][j+1])
#
#
#     maxV = 0
#     for s in lis:
#         if s > maxV:
#             maxV = s
#
#     print(f'#{tc} {maxV}')


####################################################################################
#2. 델타
# TC = int(input())
# for tc in range(1, TC+1):
#     N, M = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     dr = [-1,0,1,0]
#     dc = [0,-1,0,1]
#
#     lis =[]
#     for row in range(N):
#         for col in range(M):
#             sumV = arr[row][col]
#             for i in range(4):
#                 newR = row+dr[i]
#                 newC = col+dc[i]
#                 if newR>=0 and newR<N and newC>=0 and newC<M:
#                     sumV += arr[newR][newC]
#             lis.append(sumV)
#
#
#     maxV = 0
#     for j in lis:
#         if j > maxV:
#             maxV = j
#
#     print(f'#{tc} {maxV}')


###########################################################################

TC = int(input())
for tc in range(1, TC+1):

    N, M = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1,0,1,0]
    dc = [0,-1,0,1]

    maxV = 0
    for row in range(N):
        for col in range(M):
            cnt = arr[row][col]
            for i in range(4):
                newR = row + dr[i]
                newC = col + dc[i]
                if 0<=newR<N and 0<=newC<M:
                    cnt += arr[newR][newC]

            if cnt>maxV:
                maxV = cnt

    print(f'#{tc} {maxV}')





























