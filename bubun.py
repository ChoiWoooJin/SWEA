# TC = int(input())
# for tc in range(1, TC+1):
#     N , K = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#     n = len(arr)
#     lis = []
#     cnt = 0
#     for i in range(0,(1<<n)):
#         lis2 = []
#         for j in range(0,n):
#             if i & (1<<j):
#                 lis2.append(arr[j])
#         if sum(lis2) == K:
#             cnt += 1
#
#     print(f'#{tc} {cnt}')

#########################################
#백트래킹
#종료조건 가장 위에
#가지치기는 마지막에 작성
# def dfs(n, sm):
#
#     global ans
#     print(n, sm, ans)
#     # print(n, sm, ans)
#     # [3] 가지치기 : 더이상 정답 갱신 가능성이 없을 때 해야함
#     #가장 마지막에, 가장 위쪽에
#     # if K < sm:
#     #     return
#
#
#
#     if n == N:   #[1]종료조건(n에관련) : 반드시 정답처리는 이곳에서만!!
#         if sm ==K:
#             ans += 1
#         return
#
#     #[2] 하부호출
#     dfs(n+1, sm+lst[n])  #포함
#     dfs(n+1, sm) #포함X
#
#
#
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N , K = list(map(int, input().split()))
#     lst = list(map(int, input().split()))
#     ans = 0
#     dfs(0,0) #첫번째는 main loop 0 에서 시작, 두번쨰는 Sum 일단 0으로 시작
#
#     print(f'#{tc} {ans}')

#####################################################################
def dfs(n, sm):
    global ans
    #[3] 백트래킹(가지치기)
    if sm > K:
        return

    if sm ==K:
        ans += 1
        return

    #[1] 종료조건 먼저 작성
    if n==N:
        return

    #[2] 하부내용
    #포함(재귀)
    dfs(n+1, sm+arr[n])
    #미포함(재귀)
    dfs(n+1, sm)

TC = int(input())
for tc in range(1, TC+1):

    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = 0
    dfs(0,0)
    print(f'#{tc} {ans}')






















