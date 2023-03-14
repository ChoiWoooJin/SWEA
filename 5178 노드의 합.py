TC = int(input())
for tc in range(1, TC+1):

    N, M, L = list(map(int, input().split()))

    tree = [0] * (N+1)


    for i in range(M):
        leaf_nod_num, value = list(map(int, input().split()))
        tree[leaf_nod_num] = value   # 리프 노드에 값 할당

    # print(tree)


    # while tree.count(0) != 1:

    # lis = [0]*(N+1)
    lis =[0]* (N+1)
    # for j in range(N-M):
    sumV = 0
    for s in range(N,-1,-1):
        if tree[s] != 0:
            t = s//2
            tree[t] += tree[s]

    # print(tree)

    print(f'#{tc} {tree[L]}')






# print(tree[L])