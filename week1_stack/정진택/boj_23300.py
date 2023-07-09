# 7/1
# 스택
# 백준 23300번 웹 브라우저 2 : https://www.acmicpc.net/problem/23300

# 접근 방법: 
# 시간 제한이 1초이므로 stdin.readline() 사용함.
# 스택을 앞에 하나, 뒤에 하나 만든다. 오른쪽이 앞이고 왼쪽이 뒤이다.
# 뒤로가기의 경우(B) 앞의 스택에 현재 수를 넣고 뒤의 스택에서 pop을 한 수를 현재 수에 할당한다.
# 앞으로가기의 경우(F) 뒤의 스택에 현재 수를 넣고 앞의 스택에서 pop한 수를 현재 수에 할당한다.
# 웹 페이지에 접속할 경우(A) 현재 수를 뒤 스택에 push하고
# A 다음에 입력한 수를 현재 수에 할당한다.
# 압축을 실행할 경우 (C) 새로운 뒤 스택을 만들고 원래의 뒤 스택에서
# 하나씩 pop을 수행하면서 새로운 뒤 스택에 push한다. 이때 새로운 스택의 top과 같은 수는 push하지 않고 무시한다.
# 명령을 모두 수행한 후 뒤 스택과 앞 스택에서 하나씩 꺼내서 출력한다.
# 이때 가장 최근에 방문한 순서대로 페이지의 번호를 출력해야하므로 뒤 스택을 reverse해준다.
# 앞 스택은 사실 반대로 뒤집어서 사용했기 때문에 마찬가지로 reverse 후에 출력을 진행한다.

from sys import stdin
back = []
front = []
cur = 0
n, q = map(int, stdin.readline().split())
for _ in range(q):
    inp = stdin.readline().split()
    command = inp[0]
    if command == "B":
        if len(back) != 0:
            front.append(cur)
            cur = back.pop()
    elif command == "F":
        if len(front) != 0:
            back.append(cur)
            cur = front.pop()
    elif command == "A":
        front = []
        if cur > 0:
            back.append(cur)
        cur = int(inp[1])
    elif command == "C":
        new_back = []
        while(back):
            tmp = back.pop(0)
            if not new_back or tmp != new_back[-1]:
                new_back.append(tmp)
        back = new_back

print(cur)

if back:
    back.reverse()
    for i in back:
        print(i, end=" ")
    print()
else:
    print(-1)

if front:
    front.reverse()
    for i in front:
        print(i, end=" ")
    print()
else:
    print(-1)    