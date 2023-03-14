import sys
sys.stdin = open('input (27).txt', 'r')


# def bubblesort(arr):
#     for i in range(len(arr)-1,0,-1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less, more, equal = [], [], []
    for each in arr:
        if each < pivot:
            less.append(each)
        elif each > pivot:
            more.append(each)
        else:
            equal.append(each)
    return quick_sort(less) + equal + quick_sort(more)


arr = list(map(int, input().split()))

A = quick_sort(arr)

print(A[500000])





