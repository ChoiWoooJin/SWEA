# TC = int(input())
# for tc in range(1, TC+1):
#
#     N, M, K = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#
#     max_T = max(arr)
#     sec = [0]*(max_T+1)
#
#     for i in arr:
#         sec[i] += 1
#
#     count = 0
#     for i in sec:
#         if i >0:
#             count += 1
#
#     boong = 0
#     cnt = 0
#     for s in range(0, max_T+1):
#         if s % M == 0 and s > 0:
#             boong += K
#
#         if boong >= sec[s] and sec[s] != 0:
#             cnt += 1
#             boong -= sec[s]
#
#
#     if cnt == count:
#         print(f'#{tc} Possible')
#     else:
#         print(f'#{tc} Impossible')


################################################################
TC = int(input())
for tc in range(1, TC+1):

    N, M, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr = sorted(arr)

    max_t = max(arr)

    boong_lis = [0]*(max_t+1) # 시간대 별로 붕어빵 cnt 만들어줌
    for i in arr:
        boong_lis[i] += 1
    # print(boong_lis)

    cnt2 = 0
    for i in boong_lis:
        if i > 0:
            cnt2+=1
    # print(cnt2)

    cnt = 0
    boong = 0
    for i in range(max_t+1):
        if i % M == 0 and i > 0:
            boong += K
            # print(boong)

        if boong_lis[i] > 0:
            if boong >= boong_lis[i]:
                boong = boong - boong_lis[i]
                cnt += 1
    # print(cnt)

    if cnt == cnt2:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')


































