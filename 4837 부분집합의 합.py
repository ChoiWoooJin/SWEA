TC = int(input())

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(1, TC+1):
    N, K = list(map(int, input().split()))

    n = len(arr)
    lis = []
    for i in range(1<<n):
        result = []
        for j in range(n):
            if i & (1<<j):
                result.append(arr[j])
        if len(result) == N and sum(result) == K:

            lis.append(result)

    print(f'#{tc} {len(lis)}')







