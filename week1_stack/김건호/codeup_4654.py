import sys

def tower(n):
    tower_input= map(int, sys.stdin.readline().rstrip().split(" "))
    
    tower_list= [list(pair) for pair in zip(list(range(1,n+1)),list(tower_input))]
    #print(tower_list)
    stack = []

    for i in tower_list :
        tower_count=0
        if len(stack) == 0 :
            tower_count=0
            stack.append(i)
        else :
            top=stack[-1][1]
            if top>=i[1] : #새로 들어온 input이 바로 옆에 막히는 경우.
                tower_count=stack[-1][0]
                stack.append(i)
            else : #아닌 경우, top이 크거나 같을 때 까지 스택에서 pop 해야 한다. 
                while top<i[1] and len(stack)!=0:
                        stack.pop()
                        if len(stack) == 0 :
                            tower_count=0
                            break
                        top=stack[-1][1]
                        tower_count=stack[-1][0]
                stack.append(i)

        print(tower_count)


n = (int)(input())
tower(n)
    