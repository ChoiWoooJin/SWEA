TC = int(input())
for tc in range(1,TC+1):
    N = int(input())

    arr = [[1]*N for _ in range(N)]

    for i in range(0,N):
        for j in range(0,i):

            if i-1>=0 and i-1>=0 and j-1>=0:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    print(f'#{tc}')
    for l in range(N):
        lis = []
        for s in range(l+1):
            lis.append(arr[l][s])
        print(*lis)



