def enq(item):
    global last
    last += 1
    tree[last] = item
    c = last
    p = c//2
    while p>=1 and tree[c] < tree[p]:
        tree[c], tree[p] = tree[p], tree[c]
        c = p
        p = c//2

TC = int(input())
for tc in range(1, TC+1):

    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0]*(N+1)
    last = 0
    for item in lst:
        enq(item)
    print(tree)


    lastt = tree[-1]
    sumV = 0
    while True:
        idx = tree.index(lastt)
        idx = idx//2
        sumV += tree[idx]
        if idx == 1:
            break
        # sumV += tree[idx]
        lastt = tree[idx]

    print(f'#{tc} {sumV}')


