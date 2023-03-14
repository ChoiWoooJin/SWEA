def dfs(S, E):
    ST = []
    visited = [False] * (V+1)
    ST.append(S)
    visited[S] = True
    while ST:
        v = ST.pop()
        # if v == E:
        #     return 1

        # for w in G[v]
        for w in range(V+1):
            if G[v][w] and not visited[w]:
                if w == E:
                    return 1

                ST.append(w)
                visited[w] = True

    return 0

TC = int(input())
for tc in range(1, TC+1):
    V, E = list(map(int, input().split()))

    G = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        v1, v2 = list(map(int, input().split()))
        G[v1][v2] = 1

    v_1, v_2 = list(map(int, input().split()))

    print(f'#{tc}', dfs(v_1,v_2))


