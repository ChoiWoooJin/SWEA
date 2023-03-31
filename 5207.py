def binS(key):
    l=0
    r=len(arrA)-1
    while l<=r:
        m = (l+r)//2
        if arrA[m] == key:
            return m  #인덱스 반환
        if arrA[m]<key:
            l = m+1
        else:
            r = m-1
    return -1

def binS2(key):
    l=0
    r=len(arrA)-1
    tmp = '1'
    while l<=r:

        m = (l+r)//2
        if arrA[m] == key:
            return 1  #오른쪽 왼쪽 번갈아 왔으면 1출력
        if arrA[m]<key and (tmp=='1' or tmp =='right'):
            tmp = 'left'
            l = m+1
        elif arrA[m]>key and (tmp=='1' or tmp=='left'):
            tmp = 'right'
            r = m-1
        else:
            return 0 #번갈아 안되면 0출력

    return 0




TC = int(input())
for tc in range(1, TC+1):

    N, M = list(map(int, input().split()))
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))

    arrA = sorted(arrA)

    cnt = 0
    for i in arrB:
        a = binS(i)
        # print(a)
        if a != -1:
            ans = binS2(i)
            # print(ans)
            if ans == 1:
                cnt += 1

    print(f'#{tc} {cnt}')



