TC = int(input())
for tc in range(1, TC+1):

arr = [list(map(int, input().split())) for _ in range(100)]

arr.replace('0','')