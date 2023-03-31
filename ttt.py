#이진
# lst = [2,4,7,9,11,19,23]
# def binS(key):
#     l=0
#     r=len(lst)-1
#     while l<=r:
#         m = (l+r)//2
#         if lst[m] == key:
#             return m
#         if lst[m]<key:
#             l = m+1
#         else:
#             r = m-1
#     return -1
#
#
#
# print(binS(7))
# print(binS(23))
# print(binS(1))
# print(binS(24))


#######################################################
#이진 재귀
# lst = [2,4,7,9,11,19,23]
# def binS_r(key, l ,r):
#     global res
#
#     if l>r:
#         return
#     m = (l+r)//2
#     if lst[m] == key:
#         res = m
#         return m
#     if lst[m]<key:
#         binS_r(key, m+1, r)
#     else:
#         binS_r(key, l, m-1)
#     return
#
# N = len(lst)
#
# res = -1
# print(binS_r(7,0,N-1))
# print(res)
#
# res = -1
# print(binS_r(23,0,N-1))
# print(res)
#
# res = -1
# print(binS_r(1,0,N-1))
# print(res)
#
# res = -1
# print(binS_r(24,0,N-1))
# print(res)

#################################################
#트리

def preorder(root):
    if root:
        print(root)
        preorder(TREE[root][0])
        preorder(TREE[root][1])


N=12
V=13

strV = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, strV.split()))
TREE = [[0, 0] for _ in range(V+1)]
for i in range(0, len(lst), 2):
    p=lst[i]
    c=lst[i+1]
    if TREE[p][0] == 0:
        TREE[p][0] =c
    else:
        TREE[p][1] =c
print(TREE)


preorder(0)
print(TREE)