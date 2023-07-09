# 7/1
# 스택
# 백준 17162번 가희의 수열놀이 (Small) : https://www.acmicpc.net/problem/17162

# 접근방법 : 
# 시간제한이 1초이므로 stdin.readline()을 사용한다.
# 처음에 스택과 0으로 구성된 리스트를 하나씩 만들어 스택에 입력받은 수만큼 반복문을 돌면서
# 숫자들을 스택에 넣는 것과 동시에 해당 숫자를 mod로 나누기 연산한 수를 인덱스로 하여 리스트의 인덱스에 해당하는 값에
# 1씩을 더해주었다. 그리고 pop 연산시에는 스택에서 pop을 해주고 리스트에서 해당 인덱스의 값에 1씩 감소시켰다.
# 그러고 사용자가 3을 입력하면 스택과 리스트에 대해 이중 for문을 돌게 하여 스택의 각 숫자에 대해 나누기 연산에 해당하는
# 인덱스를 이용하여 리스트의 해당 인덱스 값을 탐색해 한번이라도 0이 나오면 -1을 출력하고 0이 나오지 않고 모든 인덱스 값이 
# 1이상임을 확인했을 때 스택에서 몇개의 수를 탐색했는지를 출력하였다. 그런데 시간초과라는 문제가 발생했고
# 이를 고치기 위해서 리스트를 만들때 각각의 인덱스에 리스트를 넣고 그 리스트에는 스택에 수를 넣을때 스택의 길이만큼의 수를
# 추가하였다. pop을 할때에는 리스트의 해당인덱스의 리스트의 마지막 원소를 pop하였다.
# 이런식으로 했을때 리스트에 대해 반복문을 돌면서 만약 하나라도 비어있으면 -1을 출력하고
# 그게 아니라면 리스트의 끝 원소들 중에서 가장 작은 수를 찾는다. 
# 그리고 배열의 총 길이에서 이 수를 빼고 출력하는 방법으로 문제를 해결하였다. 


from sys import stdin
arr=[]
query_num, mod = map(int, stdin.readline().split())
lst = [[] for _ in range(mod)]
for i in range(query_num):
    line = list(map(int, stdin.readline().split()))
    if line[0] == 1:
        lst[line[1]%mod].append(len(arr))
        arr.append(line[1])
    elif line[0] == 2:
        if arr:
            x = arr.pop()
            lst[x%mod].pop()
    else:
        count = len(arr)
        chk = 1 
        for i in lst: #시간초과 고려
            if not i:
                print(-1)
                chk = 0
                break
            count = min(i[-1],count)
        if chk:
            print(len(arr)-count)
    