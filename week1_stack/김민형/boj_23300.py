def Backward(B, F, C):
    if B == []: return B, F, C
    else:
        F.append(C)
        C = B.pop()  # 안되던 이유 1 : append와 pop 순서를 바꿔야했었음.
        return B, F, C

def Frontward(B, F, C):
    if F == []: return B, F, C
    else:
        B.append(C)
        C = F.pop()
        return B, F, C

def Access(B, x: list, C):
    if B == [] and C == 0: return [], int(x[1])
    else:
        B.append(C)
        C = int(x[1])
        return B, C # 안되던 이유 2 : B를 써야하는데 back_stack으로 했었음. 아마 Rename 도중 바뀐듯함

def Compress(Stack):
    if Stack == []: return []
    else:
        temp = []
        for idx, i in enumerate(Stack):
            if idx == 0: temp.append(i)
            else:
                if temp[-1] == i: continue
                else: temp.append(i)
        return temp

def empty_check(Stack):
    if Stack == []: return -1
    else: return Stack

N, Q = map(int, input().split())
back_stack, front_stack, Cur = [], [], 0
for i in range(Q):
    x = list(input().split())
    if x[0] == 'B': back_stack, front_stack, Cur = Backward(back_stack, front_stack, Cur)
    elif x[0] == 'F': back_stack, front_stack, Cur = Frontward(back_stack, front_stack, Cur)
    elif x[0] == 'C':
        back_stack = Compress(back_stack)
    else:
        front_stack = []
        back_stack, Cur = Access(back_stack, x, Cur)

back_stack, front_stack = empty_check(back_stack), empty_check(front_stack)
print(int(Cur))

if back_stack != -1:
    back_stack.reverse()
    for i in back_stack:
        print(int(i), end = ' ')
    print("")
else: print(-1)

if front_stack != -1:
    front_stack.reverse()
    for i in front_stack:
        print(int(i), end = ' ')
    print("")
else: print(-1)
