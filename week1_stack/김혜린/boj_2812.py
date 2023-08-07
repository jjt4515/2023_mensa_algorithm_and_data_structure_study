## import lib
import sys

## main
num, delete_num = map(int, sys.stdin.readline().split())
input_num = sys.stdin.readline().split()[0]
number_stack = []

# 나중에 delete_num이 다 안빠질 수도 있어서 체크용
left = len(input_num) -1
for i in range(len(input_num)):
    if delete_num == 0:
    	# 다 빠졌다면 끝내고 남은 숫자 수 left에 저장
        left = i
        break
    # delete_num > 0 이라면 앞에 수가 나보다 클때까지, 계속 제거할 수 있음
    while(len(number_stack)):
        if delete_num == 0:
            break
        if number_stack[-1] < int(input_num[i]):
            number_stack.pop()
            delete_num -= 1
        else:
            break
    number_stack.append(int(input_num[i]))

# 만약 delete_num이 남아있다면 스택에서 초과한만큼 제거,,
if left >= len(input_num)-1:
    if delete_num > 0:
        while (delete_num):
            number_stack.pop()
            delete_num -= 1
    total = 0
    i = 1
else:
    total = int(input_num[left:])
    i = 10**(len(input_num[left:]))

# 10단위로 늘려가면서 pop 하면서 더하기~
while(len(number_stack) != 0):
    total += i * (number_stack.pop())
    i *= 10
print(total)
