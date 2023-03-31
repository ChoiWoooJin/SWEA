def solve(k, remain, cnt):
    global minV

    if cnt >= minV:
        return


    if k ==lst[0]:
        if minV>cnt:
            minV = cnt
        return



    if remain==0:
        return


    solve(k+1, lst[k+1], cnt +1)
    solve(k+1, remain-1, cnt)

TC = int(input())
for tc in range(1, TC+1):

    lst = list(map(int, input().split())) +[0]
    minV = lst[0]
    solve(1, lst[1],0)
    print(f'#{tc} {minV}')

