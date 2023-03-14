def dfs(row, col):
    ST = []
    visited = [[False]*N for _ in range(N)] #방문 내역 배열 만들어주기

    ST.append((row, col))  # append 하나밖에 안됨 그래서 튜플로 묶어서 넣어줌
    visited[row][col] = True  # 시작점 True 로 바꿔주기
    while ST:  #ST의 길이가 0보다 클때 동안
        row , col = ST.pop()  # v[0], v[1] 쓰기 귀찮아서
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]: # 한번씩 다 들리는대
            newR = row + dr
            newC = col + dc  #연결된 새로운 좌표


            #조건 -> 새로운 좌표의 범위 지정, 1이 아닌 거 지날 때만 성립가능 그리고 visited가 False인 것만 통과 가능
            if 0<=newR<N and 0<=newC<N and ARR[newR][newC] != 1 and not visited[newR][newC]:
                if ARR[newR][newC] == 3:  # 도착지점에 도달했을 때
                    return 1
                ST.append((newR, newC))
                visited[newR][newC] = True
    return 0


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int, input().strip())) for _ in range(N)]

    # 스타트점 찾기
    for row in range(N):
        if 2 in ARR[row]:
            col = ARR[row].index(2)
            break

    print(f'#{tc}', dfs(row,col))
















