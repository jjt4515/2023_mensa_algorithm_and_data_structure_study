def cow(n) :
    stack=[]
    count=0
    for i in range(0,n) :
        cow_input = (int)(input())
        if len(stack)==0 or stack[-1]>cow_input : 
            pass
        elif stack[-1]<=cow_input : #stack.empty()==false임.
            while len(stack)!=0 and stack[-1]<=cow_input:
                stack.pop()
        count+=len(stack)
        stack.append(cow_input) 
    return count

n=int(input())
print(cow(n))
