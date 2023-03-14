TC = int(input())
for tc in range(1, TC+1):

    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))


    for i in range(M):
        a = arr.pop(0)
        arr.append(a)

    print(f'#{tc} {arr[0]}')