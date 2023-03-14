case_num = int(input())

for a in range(1, case_num+1):
    N = int(input())
    ai = list(map(int, input().split()))
    maxV = 0
    for i in ai:
        if i > maxV:
            maxV = i

    minV = 1000000000
    for s in ai:
        if s < minV:
            minV = s

    print(f'#{a} {maxV-minV}')
