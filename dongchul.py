from itertools import combinations, permutations
#
# TC = int(input())
# for tc in range(1, TC+1):

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

lis = []
for i in range(N):
    lis.append(i)

com_lis = list(permutations(lis, N))
print(com_lis)

ans_lis = []
for j in com_lis:
    per = 1.0
    for i in range(N):

        per *= (arr[i][j[i]])*(1/100)
    ans_lis.append(per)

ans_lis2 = []
for i in ans_lis:
    ans_lis2.append(i*100)

# print(ans_lis2)
an = max(ans_lis2)

ans = format(an, ".6f")
# # print(f'#{tc} {ans}')
print(ans)


# 플래그
# for i in range(N):
#     falg =False
#     for j in range(N):
#         flag = True
#         break
#     if flag:
#         break



