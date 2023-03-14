TC = int(input())
for tc in range(1, TC+1):

    arr = [list(input()) for _ in range(5)]

    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    lis2 = []
    for i in arr:
        if len(i) < max_len:
            while len(i) != max_len:
                i.append('#')
            lis2.append(i)
        else:
            lis2.append(i)


    res = []
    for row in range(max_len):
        lis = []
        for col in range(5):
            if lis2[col][row] == '#':
                continue
            else:
                lis.append(lis2[col][row])

        res.append(lis)

    ans = sum(res, [])
    ans = ''.join(map(str, ans))
    print(f'#{tc} {ans}')






