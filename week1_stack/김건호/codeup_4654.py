"""
코드업 4654번 탑 : https://codeup.kr/problem.php?id=4654    
    
접근방법 : 큰 input n개가 주어짐.
중첩 리스트를 사용해서 몇 번째 input인지 표기함. c++ vector<pair<int,int>> 같은 형식.
이후 새로운 input이 제일 최근에 들어온 원소의 길이보다 작다면, 그 input은 바로 옆의 탑을 볼 수 있음.
아닌 경우에는, input의 길이보다 크거나 같은 탑을 찾아야 한다. 
현재의 input보다 작은 탑의 경우, 앞으로의 input에 대해서 고려하지 않아도 된다. 
왜냐하면 현재의 input이 막고 있기 때문.
따라서 stack을 사용해서 pop을 할 예정.

input의 길이가 상당히 크므로, import sys 후 readline을 사용해서 입력을 읽음. 
"""

import sys

def tower(n):
    tower_input= map(int, sys.stdin.readline().rstrip().split(" "))
    
    tower_list= [list(pair) for pair in zip(list(range(1,n+1)),list(tower_input))]
    #print(tower_list)
    stack = []

    for i in tower_list :
        tower_count=0
        if len(stack) == 0 :
            tower_count=0 #스택이 비었다면 바로 추가. 
        else :
            top=stack[-1][1]
            if top>=i[1] : #새로 들어온 input이 바로 옆에 막히는 경우.
                tower_count=stack[-1][0]
                
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
