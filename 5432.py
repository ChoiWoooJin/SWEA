TC =  int(input())
for tc in range(1, TC+1):
    st = input()
    ans = cnt =0
    for i in range(len(st)):
        if st[i]=='(':   #막대기가 시작 또는 레이저 표시
            cnt += 1
        else:   #')' 바로 앞에 기호를 확인해야 되는 경우
            if st[i-1] == '(':  # 레이져
                cnt -= 1
                ans += cnt
            else:             # 막대기의 끝
                cnt -= 1
                ans += 1
    print(f'#{tc} {ans}')










###############################################################
# TC = int(ibput())
# for tc in range(1, TC+1):

arr = input()
for i in arr:





















