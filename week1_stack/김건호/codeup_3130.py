"""
코드업 3130번 소들의 헤어스타일 : https://www.codeup.kr/problem.php?id=3130

접근방법 : input n이 주어질 때 (1 <= N <= 80,000) input을 저장 후, 탐색 실시.
이러한 방법은 최악의 경우 (모든 input이 내림차순으로 정렬 된 경우), 80000^2의 탐색을 실시함.
O(n^2)의 탐색으로는 해결 불가능임.
따라서 생각을 바꾸어야 함.
내가 몇 명을 보는 것이 아닌, 나를 몇 명이 볼 수 있는가로 관점을 바꿈.
맨 처음 input을 볼 수 있는 소는 존재하지 않음.
다음 input을 볼 수 있는 소는, 전에 들어온 소 밖에 존재하지 않는다.
즉, 이후의 입력은 고려하지 않아도 된다.
시점 t에서 input_t라는 input이 들어왔다고 가정함.
시점 1, 2, 3, , .. ,t-1의 시점에 들어온 소들만 고려하면 되는데,
시점 n에 들어온 소를 고려한다고 가정하자. (입력 input_n)
시점 n+a (단, a>1이고, n+a<t라고 가정, 입력 input_(n+a))에 들어온 소가 시점 n에 들어온 input input_n보다 크다면
시점 n에 들어온 소는 시점 t에 들어온 소를 고려하지 않아도 된다.

즉, 새로운 input에 대해서, 기존의 최근에 들어온 원소가 만약 새로운 input보다 크면 새로운 input을 볼 수 있고,
작거나 같으면 저장되어 있던 소들 중, 새로운 input보다 작거나 같은 소들은 앞으로 고려하지 않아도 된다.
-> 이러한 방법을 사용해서 연산을 줄이기 가능하다!

이를 위해서 stack 자료구조를 사용했고, 자세한 내용은 아래 주석 참조.
    
    
"""


def cow(n) :
    stack=[] #스택으로 사용할 list 
    count=0 
    for i in range(0,n) : #입력받은 n번에 대해서
        cow_input = (int)(input()) #입력 후,
        if len(stack)==0 or stack[-1]>cow_input :  #만약 스택이 비어있거나, 스택 최상단의 소가 새로운 입력보다 큰 경우. 즉 보기 가능한 경우
            pass 
        elif stack[-1]<=cow_input : 
            #스택에는 소가 있고, 최상단의 소가 새로운 입력보다 작거나 같은 경우
            #이러한 경우, 입력보다 작은 소들은 앞으로 나올 input에 대해서 영향을 주지 않음.
            #연산을 줄이기 위해서 pop을 한다.
            while len(stack)!=0 and stack[-1]<=cow_input:
                stack.pop()
        count+=len(stack)  #스택에 남아 있는 소의 수가 input을 볼 수 있는 소의 수.
        stack.append(cow_input) #이후 새롭게 들어온 소를 추가한다.
    return count

n=int(input())
print(cow(n))
