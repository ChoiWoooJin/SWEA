tc = int(input())
K = 9

for j in range(1, tc+1):
    N = int(input())
    nums = list(map(int, input()))

    counts = [0] * (K + 1)
    for num in nums:
        counts[num] += 1


    minV = 0
    for i in range(10):
        if minV <= counts[i]:
            minV = counts[i]
            idx = i

    print(f'#{j} {idx} {minV}')


