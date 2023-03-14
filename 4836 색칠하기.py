# TC = int(input())
# for tc in range(1,TC+1):
#
#     N= int(input())
#
#     brd =[[0]*10 for i in range(10)]
#
#     for q in range(N):
#         r1, c1, r2, c2, color = list(map(int, input().split()))
#         for i in range(r1, r2 + 1):
#             for j in range(c1, c2 + 1):
#                 brd[i][j] = brd[i][j] + color
#     cnt = 0
#     for p in range(10):
#         for c in range(10):
#             if brd[p][c]==3:
#                 cnt += 1
#
#     print(f'#{tc} {cnt}')


#############################################################################
# TC = int(input())
# for tc in range(1,TC+1):
#     N = int(input())
#     arr = [[0]*10 for _ in range(10)]
#     for i in range(N):
#         r1, c1, r2, c2, color = list(map(int, input().split()))
#
#         for r in range(r1, r2+1):
#             for c in range(c1, c2+1):
#                 arr[r][c] += 1
#     cnt = 0
#     for j in arr:
#         for n in j:
#             if n>1:
#                 cnt += 1
#
#     print(f'#{tc} {cnt}')


##############################################################################


TC = int(input())
for tc in range(1, TC+1):

    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color

    # print(arr)

    cnt = 0
    for row in range(10):
        for col in range(10):
            if arr[row][col] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')




























