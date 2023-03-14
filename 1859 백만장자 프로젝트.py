# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#
#     i = ans = 0
#     while i < N:
#         # [1] i~ 끝까지 최댓값의 index 찾기
#         i_mx = i
#         for j in range(i+1, N):
#             if lst[i_mx]<lst[j]:
#                 i_mx = j
#         # [2] i~i_mx 까지의 최대값과의 차이 누적
#         for j in range(i, i_mx):
#             ans += lst[i_mx] - lst[j]
#
#         i = i_mx + 1
#
#
#     print(f'#{tc} {ans}')


###########################################
#입력값 뒤쪽부터 받기

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1] # 읽을 떄 반대로 일기

    mx = ans = 0
    for n in lst:
        if mx > n:
            ans += mx-n
        else:
            mx = n

    print(f'#{tc} {ans}')
