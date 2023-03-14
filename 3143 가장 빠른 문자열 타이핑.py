def brute(T, P, st):
    lenP = len(P)  # 찾는 문자
    lenT = len(T)  # 전체 문자

    for idxT in range(st, lenT - lenP + 1):
        idxP = 0

        while idxP < lenP and T[idxT + idxP] == P[idxP]:
            idxP += 1


        if idxP == lenP:
            return idxT

    return -1


TC = int(input())
for tc in range(1, TC+1):
    A, B = list(input().split())
    T = A


    lis = []
    r = 0
    while True:
        r = brute(T, B, r)
        if r==-1 :
            break
        lis.append(r)
        r += len(B)

    a = len(lis)

    print(f'#{tc} {len(A) - (len(B)*a) +a}')




###################################################
# T = int(input())
# for tc in range(1, T + 1):
#     A, B = input().split()
#     N = len(A)
#     M = len(B)
#     i = 0
#     cnt = 0
#
#     while i < N:
#         if A[i] == B[0]:
#             if A[i:i + M] == B:
#                 cnt += 1
#                 i += M
#             else:
#                 cnt += 1
#                 i += 1
#         else:
#             cnt += 1
#             i += 1
#     print(f'#{tc} {cnt}')








