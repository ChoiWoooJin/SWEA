TC = int(input())
for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))
    Ci = [0] + list(map(int, input().split()))

    nextP = 1
    Oven = [(0,0)] * N
    while Oven:
        no, c = Oven.pop(0) # 1번화덕의 피자 치즈량
        c = c//2
        if c > 0:
            Oven.append((no,c))
            #
        else:
            if nextP <= M:
                Oven.append((nextP, Ci[nextP])) # 다음 피자의 치즈
                nextP += 1

    print(f'#{tc} {no}')
###################################################################
# # TC = int(input())
# N, M = list(map(int, input().split()))
# Ci = [0] + list(map(int, input().split()))
# nextP = 1
# Oven = [(0,0)]*N
# for i in Ci:
#     Oven.append()



