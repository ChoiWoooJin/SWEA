# TC = int(input())
# for tc in range(1, TC+1):
#
#     N , M = list(map(int, input().split()))
#     arr = [list(map(int, input().split()))for _ in range(N)]
#
#
#     lis2 = []
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             lis = []
#             for l in range(M):
#                 for s in range(M):
#                     lis.append(arr[i+s][j+l])
#
#             lis2.append(sum(lis))
#
#
#     maxV = 0
#     for a in lis2:
#         if a > maxV:
#             maxV = a
#
#     print(f'#{tc} {maxV}')
#######################################################
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N, M = list(map(int, input().split()))
#
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     lis =[]
#     for row in range(N-M+1):
#         for col in range(N-M+1):
#             sumV = 0
#             for i in range(M):
#                 for j in range(M):
#                     sumV += arr[row+i][col+j]
#             lis.append(sumV)
#
#
#     maxV = 0
#     for s in lis:
#         if s > maxV:
#             maxV = s
#
#     print(f'#{tc} {maxV}')

##########################################################################

TC = int(input())
for tc in range(1, TC+1):

    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]


    maxV = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            cnt = 0
            for i in range(M):
                for j in range(M):
                    cnt += arr[row+i][col+j]

            if cnt > maxV:
                maxV = cnt


    print(f'#{tc} {maxV}')
























