TC = int(input())
for tc in range(1, TC+1):

    s = input()
    s = s.rstrip()
    if s == s[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')



# def isPelindrome(s):
#     s = s.rstrip()
#     lenS = 0
#     for _ in s:
#         lenS += 1
#     for idx in range(lenS//2):
#         if s[idx] != s[lenS-1-idx]:
#             return 0
#     return 1

