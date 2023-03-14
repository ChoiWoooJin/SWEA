# # TC = int(input())
# # # for tc in range(1,TC+1):
# # N = int(input())
# arr = list(map(int,input().split()))
# #
# # # # print(arr)
# # #
# # lis = []
# # a=-1
# # for i in range(len(arr)):
# #     if i%2 == 0:
# #         lis.append(arr[a])
# #         a=a-1
# #
# #     else:
# #         lis.append(arr[i-1])
# # print(lis)
#
#
#
# #
# #
# #
# #
# #
# #     else:
#
#
#
# # print(lis)
#
# ########
# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] > arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
#
# print(selection_sort(arr))
#
#
#
#
#
#
#
# # # print(select(arr,3))
# lis = []
# for m in range(len(arr)):
#     if m%2 == 0
#     lis.append(selection_sort(arr[m]))
# print(lis)


#############################################################################
def bs(arr, L):
    for i in range(L-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    L = len(arr)
    arr_sort = bs(arr,L)
    arr_sort_t = arr_sort[::-1]
    lis = []
    for p in range(L//2):
        lis.append(arr_sort_t[p])
        lis.append(arr_sort[p])
        if len(lis) == 10:
            break

    lis = ' '.join(map(str, lis))
    print(f'#{tc} {lis}')













