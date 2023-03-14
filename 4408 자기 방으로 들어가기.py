
# (방번호 -1) // 2 : 복도 번호
# [1] 시작 복도 번호 ~ 끝 복도 번호 : 누적 cnt 표시
# [2] 최대값 찾기


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())


    cnt = [0] * 200
    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:     # 중요 예외 (스타트가 엔드보다 클 수 있음)
            s, e = e, s
        for j in range((s-1)//2, (e-1)//2+1):
            cnt[j] += 1

    res = max(cnt)
    print(f'#{tc} {res}')