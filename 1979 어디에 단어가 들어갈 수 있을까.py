# N, K = list(map(int, input().split()))

# arr = []
# for i in range(5):
#     arr.append(list(map(int, input().split())))
#
#
# lis = []
# cnt = 0
# for row in range(5):
#
#     for col in range(5):
#         if arr[row][col] == 1:
#             cnt += 1
#         elif arr[row][col] == 0:
#             cnt += 0
#     lis.append(cnt)
# print(lis)


# lis2 = []
# for row in range(5):
#     cnt2 = 0
#     for col in range(5):
#         if arr[col][row] == 1:
#             cnt2 += 1
#     lis.append(cnt2)
#
# print(lis2)


def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:  # 단어를 넣을 수 있는 공백
                cnt += 1
            else:  # 칸 없음!
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]

    # arr와 arr_t 로 각각 개수를 계산
    arr_t = list(map(list, zip(*arr)))
    ans = count(arr) + count(arr_t)
    print(f'#{test_case} {ans}')


