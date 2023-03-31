#startlink

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

nums = []
for i in range(n):
    nums.append(i)
# print(nums)


answer_list = []

def nCr(n, ans, r):
    if n == len(nums):
        if len(ans) == r:
            temp = [i for i in ans]
            answer_list.append(temp)
        return
    ans.append(nums[n])
    nCr(n + 1, ans, r)
    ans.pop()
    nCr(n + 1, ans, r)

def nCr1(n, ans, r):
    if n == len(start):
        if len(ans) == r:
            temp = [i for i in ans]
            start_list.append(temp)
        return
    ans.append(start[n])
    nCr1(n + 1, ans, r)
    ans.pop()
    nCr1(n + 1, ans, r)

def nCr2(n, ans, r):
    if n == len(num):
        if len(ans) == r:
            temp = [i for i in ans]
            num_list.append(temp)
        return
    ans.append(num[n])
    nCr2(n + 1, ans, r)
    ans.pop()
    nCr2(n + 1, ans, r)

nCr(0, [], n//2)
lis = answer_list
# print(lis)

lis2= []
for start in lis:
    stat1 = 0
    stat2 = 0
    start_list = []

    nums = []
    for i in range(n):
        nums.append(i)

    for i in start:
        nums.remove(i)

    num = nums
    num_list = []

    nCr1(0,[],2)
    nCr2(0,[],2)
    # print(start_list)
    # print(num_list)

    for i in start_list:
        stat1 += arr[i[0]][i[1]] + arr[i[1]][i[0]]

    for j in num_list:
        stat2 += arr[j[0]][j[1]] + arr[j[1]][j[0]]

    lis2.append(abs(stat1-stat2))
print(min(lis2))









