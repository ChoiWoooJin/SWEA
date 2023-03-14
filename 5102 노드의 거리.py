def bfs(s):
    visited = [0]*(V+1)
    Q = []
    Q.append(s)
    visited[s] = 1
    while Q:
        t = Q.pop(0)
        for w in G[t]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[t] + 1

    return visited

# visited[t]
TC = int(input())
for tc in range(1, TC+1):

    V, E = list(map(int, input().split()))

    lis = []
    for i in range(E):
        r, c = list(map(int, input().split()))
        lis.append(r)
        lis.append(c)

    S, R = list(map(int, input().split()))

    G = [[] for _ in range(V+1)]
    for idx in range(0, len(lis), 2):
        p1 = lis[idx]
        p2 = lis[idx+1]
        G[p1].append(p2)
        G[p2].append(p1)
    # print(G)
    # print(bfs(S))

    ans_lis = bfs(S)
    ans = ans_lis[R] - 1
    if ans == -1:
        ans = 0
    print(f'#{tc} {ans}')









