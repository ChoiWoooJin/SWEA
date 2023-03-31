# # TC = int(input())
# # for tc in range(1, TC+1):
# #
#
#
#
# def perm(i,k):   # i값을 결정할 자리, k 결정할 개수
#
#     if i == k:
#         # print(p)
#         tmp.append(p[:])
#
#     else:
#         for j in range(i,k): # 자신부터 오른쪽원소들과 교환
#             p[i], p[j] = p[j], p[i]
#             perm(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# # TC = int(input())
# # for tc in range(1, TC+1):
#
#
# arr, n = list(map(int, input().split()))
# lis = []
# tmp = []
# p = []
#
# for i in str(arr):
#     p.append(int(i))
# # print(p)
# perm(0,len(p))
#
# for i in range(n):
#     perm(0, len(p))
#     # print(max(tmp))
#     lis, tmp = tmp, lis
#
# ans = max(lis)
# ans = ''.join(map(str,ans))
# print(ans)
#     # print(f'#{tc} {ans}')



########################################


def change(k, value):
    global maxV

    if value in visited[k]:
        return
    else:
        visited[k].append(value)




    arr = list(str(value))
    L = len(arr)
    if k == N:

        if maxV < value:
            maxV = value
        return

    for i in range(L-1):
        for j in range(i+1,L):
            arr[i], arr[j] = arr[j], arr[i]
            value = int(''.join(arr))

            change(k + 1, value)
            arr[i], arr[j] = arr[j], arr[i]


TC = int(input())
for tc in range(1, TC+1):
    value, N = map(int, input().split())
    maxV = 0
    visited= {}
    for i in range(0,11):
        visited[i] = []
    change(0,value)
    print(f'#{tc} {maxV}')









