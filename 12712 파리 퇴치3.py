TC = int(input())
for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(N)]



    dr1 = [-1,0,1,0]
    dc1 = [0,-1,0,1]



    lis = []
    for row in range(N):
        for col in range(N):
            cnt = arr[row][col]

            for i in range(4):
                if i == 0:
                    for j in range(M-1):
                        newR = row + (dr1[i]-j)
                        if newR>=0 and newR<N:
                            cnt += arr[newR][col]
                if i == 1:
                    for j in range(M-1):
                        newC = col + (dc1[i]-j)
                        if newC>=0 and newC<N:
                            cnt += arr[row][newC]
                if i == 2:
                    for j in range(M-1):
                        newR = row + (dr1[i]+j)
                        if newR >= 0 and newR < N:
                            cnt += arr[newR][col]
                if i == 3:
                    for j in range(M-1):
                        newC = col + (dc1[i]+j)
                        if newC >= 0 and newC < N:
                            cnt += arr[row][newC]
            lis.append(cnt)




    dr2 = [-1, 1, 1, -1]
    dc2 = [-1,-1,1,1]

    lis2 = []
    for row2 in range(N):
        for col2 in range(N):
            cnt2 = arr[row2][col2]

            for i in range(4):
                if i == 0:
                    for j in range(M-1):
                        newR2 = row2 + (dr2[i]-j)
                        newC2 = col2 + (dc2[i]-j)
                        if newR2>=0 and newR2<N and newC2>=0 and newC2<N:
                            cnt2 += arr[newR2][newC2]
                if i == 1:
                    for j in range(M - 1):
                        newR2 = row2 + (dr2[i] + j)
                        newC2 = col2 + (dc2[i] - j)
                        if newR2 >= 0 and newR2 < N and newC2 >= 0 and newC2 < N:
                            cnt2 += arr[newR2][newC2]
                if i == 2:
                    for j in range(M - 1):
                        newR2 = row2 + (dr2[i] + j)
                        newC2 = col2 + (dc2[i] + j)
                        if newR2 >= 0 and newR2 < N and newC2 >= 0 and newC2 < N:
                            cnt2 += arr[newR2][newC2]
                if i == 3:
                    for j in range(M - 1):
                        newR2 = row2 + (dr2[i] - j)
                        newC2 = col2 + (dc2[i] + j)
                        if newR2 >= 0 and newR2 < N and newC2 >= 0 and newC2 < N:
                            cnt2 += arr[newR2][newC2]
            lis2.append(cnt2)



    a = max(lis)
    b = max(lis2)
    lis3 = [a, b]
    ans = max(lis3)
    print(f'#{tc} {ans}')




