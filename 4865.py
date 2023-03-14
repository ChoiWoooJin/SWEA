TC = int(input())
for tc in range(1, TC+1):

    str1 = list(input())
    str2 = list(input())

    lis = []
    for i in str2:
        if i in str1:
            lis.append(i)


    count = {}
    for i in lis:
        try: count[i] += 1
        except: count[i] = 1


    maxV = 0
    for i in count:
        if count[i] > maxV:
            maxV = count[i]
    print(f'#{tc} {maxV}')



