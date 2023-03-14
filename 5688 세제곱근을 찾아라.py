TC = int(input())
for tc in range(1, TC+1):

    N = int(input())

    i = 1
    while True:
        if i**3 == N:
            print(f'#{tc} {i}')
            break
        elif i**3 < N:
            i += 1
        else:
            print(f'#{tc} -1')
            break


# N = 64
# print(N**(1/3))
# print(64**(1/3))