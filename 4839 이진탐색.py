def binarySearch(a, N, key):
    start = 0
    end = N-1
    cnt = 0
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return cnt + 1
        elif a[middle] > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1
    return cnt

TC = int(input())
for tc in range(1, TC+1):
    P, Pa, Pb = list(map(int, input().split()))
    a = []
    for i in range(1, P+1):
        a.append(i)

    if binarySearch(a, P, Pa) < binarySearch(a, P, Pb):
        print(f'#{tc} A')
    elif binarySearch(a, P, Pa) == binarySearch(a, P, Pb):
        print(f'#{tc} 0')
    elif binarySearch(a, P, Pa) > binarySearch(a, P, Pb):
        print(f'#{tc} B')

###########################################################################


TC = int(input())

P, A, B = list(map(int, input().split()))
arr = []
for i in range(1,P+1):
    arr.append(i)

def binary(key,P)
    S = 0
    E = P-1
    cnt = 1
    while S <= E:
        middle = (S+E)//2
        if a[middle] == key:






























