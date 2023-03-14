tc = int(input())
divs = [2, 3, 5, 7, 11]
for t in range(1, tc+1):
    N = int(input())
    cnts = [0]*len(divs)
    for i in range(0, len(divs)):
        while N % divs[i] == 0:
            cnts[i] = cnts[i] + 1
            N = N//divs[i]
    cnts_not_list = ' '.join(map(str, cnts))

    print(f'#{t} {cnts_not_list}')







