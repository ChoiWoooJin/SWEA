# N = int(input())
# arr = list(map(int, input().split()))
# arr = sorted(arr)
# print(arr)
# max_house = max(arr)

# house = [0]*(max_house+1) #인덱스 0은 사용X

# for i in arr:
#     house[i] += 1  #집 위치 찍어주기

# lis = []
# idx_lis = []
# for i in range(len(house)):
#
#     cnt = 0
#     if house[i] >= 1:
#         # print(house)
#
#         for j in range(len(house)):
#             if house[j] >= 1:
#                 cnt += abs(i-j)
#
#         lis.append(cnt)
#         idx_lis.append(i)
#
#
# a = min(lis)
# ans = lis.index(a)
# print(idx_lis[ans])


##############################################

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

arr_len = len(arr)
# print(arr[arr_len//2])

if arr_len % 2 == 1:
    print(arr[arr_len//2])
else:
    print(arr[arr_len//2-1])














