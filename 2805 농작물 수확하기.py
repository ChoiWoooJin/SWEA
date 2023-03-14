TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    resS = 0
    col_start = N//2 + 1
    col_ran = -1

    for row in range(N):
        if row > N // 2:
            col_start += 1
            col_ran -= 2
        elif row <= N // 2:
            col_start -= 1
            col_ran += 2
        for col in range(N):
            if col == col_start:
                for i in range(col_ran):
                    resS += arr[row][col+i]

    print(f'#{tc} {resS}')





