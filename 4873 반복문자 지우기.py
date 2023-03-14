TC = int(input())
for tc in range(1, TC+1):

    string = input()
    s = []
    for i in string:
        if s != [] and i == s[-1]:
            s.pop(-1)
        else:
            s.append(i)

    print(f'#{tc} {len(s)}')













########################

# lis = list(input())
#
# for i in range(len(lis)-2):
#     if lis[i] == lis[i+1]:
#         lis.remove(lis[i + 1])
#         lis.remove(lis[i])
#
#
# print(lis)


