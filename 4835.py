case_num = int(input())
for i in range(1, case_num+1):
    N, M = list(map(int, input().split()))
    ai = list(map(int, input().split()))
    lis = []

    for a in range(N-M+1):
        sumV = 0
        for c in range(M):

            sumV += ai[a+c]
        lis.append(sumV)

    maxV = 0
    for b in lis:
        if b > maxV:
            maxV = b

    minV = 1000000000
    for s in lis:
        if s < minV:
            minV = s

    print(f'#{i} {maxV - minV}')


    # 10 3
    # 0:2 :3
    # for j in range(M):
    #
    # 1:3
    # ~ 7:9
    #
    # 10 5
    # 0:4 ~ 5:9




