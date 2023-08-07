'''
문제: AC - https://www.acmicpc.net/problem/5430 🥇5

code
1. 배열 뒤집기에서 시간복잡도가 커질 것이라고 생각해 빠르게 할 수 있는 방법 고안 -> 배열 뒤집기가 아닌 pop() 위치 뒤집기
2. 출력이 조금 까다로웠던 문제
'''

import sys

## 받고
n = int(sys.stdin.readline())

## 반복
for i in range(n):
	## 앞이 어딘지 체크하는 flag 변수
    is_front = True
    ## 현재 error 출력을 해야하는지 확인하는 flag 변수
    is_error = False
    order = sys.stdin.readline()
    num = int(sys.stdin.readline())
	
    ## 리스트가 비었으면 내가 쓴 코드가 에러떠서 만들어놓은 try-except문
    try:
        my_list = list(map(int, sys.stdin.readline()[1:-2].split(',')))
    except:
        my_list = []

    for od in order:
    	## R 만나면 뒤집기
        if od == 'R':
            if is_front:
                is_front = False
            else:
                is_front = True
        ## D 만나면 없애는데 리스트 비었는지 확인, 비면 error flag에 전달
        elif od == 'D':
            if my_list:
                if is_front:
                    my_list.pop(0)
                else:
                    my_list.pop()
            else:
                is_error = True
                break

    if is_error:
        print('error')
    else:
        if not my_list:
            print('[]')
        else:
            if is_front:
                print('[', end='')
                for i in my_list[:-1]:
                    print(i, end=',')
                print(my_list[-1], end='')
                print(']')
            else:
                print('[', end='')
                for i in my_list[::-1][:-1]:
                    print(i, end=',')
                print(my_list[0], end='')
                print(']')
