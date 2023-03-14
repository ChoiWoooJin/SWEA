tc = int(input())

for i in range(1, tc+1):
    K, N, M = map(int, input().split())
    CHS = list(map(int, input().split()))
    curV = 0
    cnt = 0
    while curV < N:
        nextV = curV + K

        if nextV >= N:
            break

        while curV < nextV and nextV not in CHS:
            nextV -= 1

        if curV == nextV:
            cnt = 0
            break

        curV = nextV
        cnt += 1

    print(f'#{i} {cnt}')


K, N, M = map(int, input().split())
CHS = list(map(int, input().split()))





