TC = int(input())
for tc in range(1, TC+1):

    N, M = list(map(int, input().split()))

    arr = [input() for _ in range(N)]


    #3개의 영역으로 구분하기
    minV = M*N
    for a in range(N-2):  #W 영역 맨 아래 0~N-3
        for b in range(a+1, N-1): #B 영역
            cnt = 0 #각 영역에서 새로 칠하는 횟수
            for i in range(0, a+1): #W영역에서
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1
            for i in range(a+1, b+1): #B영역에서
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1
            for i in range(b+1, N): #R영역에서
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1

            if minV > cnt:
                minV = cnt
    print(f'#{tc} {minV}')






