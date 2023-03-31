def dfs(n, sumk, summ):
    global maxjmt
    if sumk > L:
        return

    if n == N:
        maxjmt = max(summ, maxjmt)
        return

    dfs(n+1, sumk+K[n], summ+T[n])
    dfs(n+1, sumk, summ)


TC = int(input())
for tc in range(1, TC+1):

    N, L = list(map(int, input().split()))
    T = []
    K = []
    maxjmt = 0
    for i in range(N):
        t, k = list(map(int, input().split()))
        # print(t,k)
        T.append(t)
        K.append(k)

    dfs(0,0,0)
    print(f'#{tc} {maxjmt}')


