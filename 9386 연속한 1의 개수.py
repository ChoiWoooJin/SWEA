tc = int(input())

for j in range(1, tc+1):
    N = int(input())
    nums = list(map(int, input()))
    lis = []
    cnt = 1
    for i in range(N-1):

        if nums[i] == 1:
            if nums[i] == nums[i+1]:
                cnt += 1
                lis.append(cnt)

            else:
                cnt = 1
                lis.append(cnt)

        elif nums[i] == 0:
            pass


    maxV = 0
    for s in lis:
        if s > maxV:
            maxV = s
    print(f'#{j} {maxV}')









