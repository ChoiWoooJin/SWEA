# TC = int(input())
# for tc in range(1, TC+1):

arr = list(map(int, input().split()))

def cal(l,r):
    if r == l+1 or (r==1 and l==3):
        return r
    else:
        return l

# l과 r 사이의 가위바위보정보를 기준으로 승자의 idx를 반환
def game(l,r):
    if l== r:
        return r
    m = (l + r)//2

    lwinner = game(1,m)
    rwinner = game(m+1, r)
    t = cal(lwinner, rwinner)

    return t
