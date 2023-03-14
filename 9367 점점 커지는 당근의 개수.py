tc = int(input())
for j in range(1, tc+1):

    N = int(input())
    C = list(map(int,input().split()))
    lis = []
    cnt = 1
    for i in range(N-1):
        if C[i]+1 == C[i+1]:
            cnt = cnt + 1
            lis.append(cnt)

        else:
            cnt = 1
            lis.append(cnt)


    maxV = 0
    for s in lis:
        if s > maxV:
            maxV = s
    print(f'#{j} {maxV}')



