# def dfs(n, sm):
#     global ans
#     #최소값 구할 때 항상 성공하는 가지치기
#     # if ans<=sm-B:
#     #     return
#     if ans == 0:
#         return
#     if sm >= B:
#         ans = min(ans, sm - B)
#     return
#
#     if n==N:
#         return
#
#
#     dfs(n+1, sm+lst[n])
#     dfs(n+1, sm)
#
#
#
#
#
# #가능한 모든 경우 처리
# #n:직원번호(혹은 idx)
# TC = int(input())
# for tc in range(1,TC+1):
#     N, B = list(map(int, input().split()))
#     lst = list(map(int, input().split()))
#     ans = N*10000
#     dfs(0,0)
#     print(f'#{tc} {ans}')


#############################################################
def dfs(n, sm):
    global minV, ans

    if minV == 0:
        return

    if sm >= B:
        minV = min(minV, sm-B)
        return

    if n==N:
        return

    dfs(n+1, sm + arr[n])
    dfs(n+1, sm)

TC = int(input())
for tc in range(1, TC+1):

    N, B = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    minV = N*10000

    dfs(0,0)
    print(f'#{tc} {minV}')





















