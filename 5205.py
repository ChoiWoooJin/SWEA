# 퀵소트
def hoare(l,r):
    p=l
    lp=l+1
    rp=r
    while lp<=rp:
        while lp<=rp and lst[lp] <= lst[p]:
            lp += 1
        while lp<=rp and lst[rp] >= lst[p]:
            rp -= 1
        if lp<rp:
            lst[lp], lst[rp] = lst[rp], lst[lp]
    lst[p], lst[rp] = lst[rp], lst[p]
    return rp

def quicks(l,r):
    if l<r:
        p = hoare(l,r)
        quicks(l,p-1)
        quicks(p+1,r)


TC = int(input())
for tc in range(1,TC+1):

    N = int(input())
    lst = list(map(int, input().split()))
    quicks(0,N-1)
    print(f'#{tc} {lst[N//2]}')
