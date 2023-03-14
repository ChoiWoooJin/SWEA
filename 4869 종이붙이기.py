# TC = int(input())
# for tc in range(1, TC+1):

# fi = [0]*100
# fi[0] = 0
# fi[1] = 1
# def fibo(n):
#     if n>=2 and fi[n]>0:  # 이미 계산되어 있지 않으면
#         t1 = fibo(n-1)
#         t2 = fibo(n-2)
#         fi[n] = t1+t2
#     return fi[n]

fi = [0]*31
fi[1] = 1
fi[2] = 3
def f(num):
    if num > 2:
        fi[num] = 2*f(num-2) + f(num-1)
    return fi[num]

TC = int(input())
for tc in range(1, TC+1):

    num = int(input())
    num = int(num/10)

    print(f'#{tc}', f(num))







# fi[1] = 1
# fi[2] = 3
#
# def fi(num):
#     if num > 2:
#         fi[num] = 2*fi(num-1) + fi(num-2)
#     return fi[num]

