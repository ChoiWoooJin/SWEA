# def dfs(n, sm):
#     global ans
#     if n > 12:
#         ans = min(ans,sm)
#         return
#
#     dfs(n+1, sm+day*lst[n])
#     dfs(n+1, sm+mon)
#     dfs(n+3, sm+mon3)
#     dfs(n+12, sm+year)
#
# TC = int(input())
# for tc in range(1, TC+1):
#     day, mon, mon3, year = list(map(int, input().split()))
#     lst = [0]+list(map(int, input().split()))
#
#     #[1]백트래킹
#     ans = 365*3000
#     dfs(1,0)
#
#     print(f'#{tc} {ans}')

########################################################################
def dfs(n,sm):
    global minV
    if sm > minV:
        return

    if n > 12:
        minV = min(sm, minV)

        return

    dfs(n+1, sm+day*arr[n])
    dfs(n+1, sm+mon)
    dfs(n+3, sm+mon3)
    dfs(n+12, sm+year)


TC = int(input())
for tc in range(1, TC+1):

    day, mon, mon3, year = list(map(int, input().split()))
    arr = [0]+list(map(int, input().split()))
    minV = 365*3000
    dfs(0,0)
    print(f'#{tc} {minV}')























