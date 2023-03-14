

# dr = [-1,0,1,0]
# dc = [0,-1,0,1]

def dfs(sr, sc):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1
    while q:
        sr, sc = q.pop(0)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 한번씩 다 들리는대
            newR = sr + dr
            newC = sc + dc  # 연결된 새로운 좌표
            # if arr[newR][newC] == 3:
            #     return visited[newR][newC]
            if newR >= 0 and newR < N and newC >= 0 and newC < N and arr[newR][newC] != 1 and visited[newR][newC] == 0:
                if arr[newR][newC] == 3:
                    visited[newR][newC] = visited[sr][sc] - 1

                    return visited[newR][newC]
                else:
                    q.append((newR, newC))
                    visited[newR][newC] = visited[sr][sc] + 1


    return 0




TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sr = i
                sc = j
                break
    ans = dfs(sr, sc)
    print(f'#{tc} {ans}')








