def isPair(input_s):

    stack = []
    for i in input_s:
        if i == '(' or i == ')' or i == '{' or i == '}':

            if i == '(' or i == '{':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0:
                    return 0
                t = stack.pop(-1)
                if t != '(':
                    return 0
            elif i == '}':
                if len(stack) == 0:
                    return 0
                p = stack.pop(-1)
                if p != '{':
                    return 0
    if len(stack) > 0:
        return 0
    return 1

TC = int(input())
for tc in range(1, TC+1):
    input_s = input()
    a = isPair(input_s)


    print(f'#{tc} {a}')

