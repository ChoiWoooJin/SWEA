# TC = int(input())
# for tc in range(1, TC+1):

# exp = list(input().split())


def cal(v1,v2,op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v1 - v2
    if op == '*':
        return v1 * v2
    if op == '/':
        return v1 // v2

def step2(exp):
    ST = []
    for c in exp:
        if c.isdigit():
            ST.append(int(c))

        elif c == '+' or c == '-' or c == '*' or c == '/':

            v2 = ST.pop()
            if ST == []:
                return 'error'
            v1 = ST.pop()
            ST.append(cal(v1,v2,c))
        elif c =='.':
            if len(ST)>1:
                return 'error'
            # return ST[-1]
            return ST[-1]


TC = int(input())
for tc in range(1, TC+1):
    exp = list(input().split())
    print(f'#{tc}', step2(exp))

