#괄호 검사

def is_empty(s):
    if len(s) == 0:
        return True

def check(str_ls):
    stack = []
    for i in str_ls:
        if i == '(':
            stack.append(i)
        else:
            if is_empty(stack):
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

cnt = int(input())
for i in range(cnt):
    str_in = input()
    str_ls = [c for c in str_in]
    if check(str_ls):
        print("YES")
    else:
        print("NO")

