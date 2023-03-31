N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]


home = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i,j))
        if arr[i][j] == 2:0
            chicken.append((i,j))

print(home)
print(chicken)

ans_lis = []
for i in home:
    lis = []
    for j in chicken:
        ans = abs(i[0]-j[0])+abs(i[1]-j[1])
        lis.append(ans)
    ans_lis.append(min(lis))

print(sum(ans_lis))





