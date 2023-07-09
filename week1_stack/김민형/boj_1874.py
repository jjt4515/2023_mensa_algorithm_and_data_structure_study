# 아직 못 품 **

n = int(input())
res = []
temp = []
pp = []

for _ in range(n):
    k = 0
    k = int(input())
    res.append(k)


def check_pop(y):
    if res[y] == temp[-1]:
        print(res[y], temp[-1]) # 1
        temp.pop()
        pp.append('-')
        if len(temp) != 0:
            return check_pop(y + 1)
        elif res[y] < temp[-1]:
            return print('NO')
    return None 

def try_append(x, y):

    if x == 1:
        for ele in range(x, res[y] + 1):
            temp.append(ele)
            pp.append('+')
            if check_pop(y):
                pass
        try_append(y, pp.count('-'))
    else:
        for ele in range(res[x], res[y] + 1):
            temp.append(ele)
            pp.append('+')
            if check_pop(y):
                pass
        try_append(y, pp.count('-'))

try_append(1, 0)

print(res, '-----', temp, '-----', pp)

'''
내가 풀려고 했던 방식 : 
1. 입력 값들을 res = []에 넣는다.
2. 1부터 res[0]까지 temp = []에 append하며 pp = []에 '+'를 append한다.
3. 2번 완료시 temp[-1]과 res[0]이 같다면 pop 하고 pp에 '-' append
4. 3번 완료시 temp[-1]과 res[1]이 같다면 pop 하고 pp에 '-' append 이러한 과정 반복
5. 반복이 끝나면 첫 append의 끝 숫자인 res[0]부터 res[x] ( x == 반복이 끝난 경우의 index )까지 temp에 append 그리고 pp에 '+' append
6. 해당 경우들을 반복

문제점 :
1. check_pop 함수 동작 시 temp와 res[n] (n == 해당 함수 과정 수행 시의 정수)이 같아지는 경우가 있는데 재귀함수라 이 다음 경우에서 에러가 발생
1-1. 이 에러는 실제 'NO'를 출력해야하는 경우도 있지만 실제로 temp가 비었고 다음 res[n]까지 append 해도 문제가 없는 경우가 포함이 됨 - 코드가 복잡해지고 효율적이지 못함 실제로 이 경우부터 포기했다고 봐도 무방
2. try_append 함수를 보면 알겠지만 x == 1인 경우와 eles 경우로 나뉨.
2-1. 정확한 에러는 찾지 못하겠지만 코드가 동작하는 과정을 직관적으로 보기 너무 어려움.
2-2. 코드 내의 '#1' 부분을 통해 확인해 본 결과, append 자체는 잘되는걸 확인할 수 있음. 하지만 check_pop 함수와 연관지어 작동 과정을 생각하기 어려움

총평 :
풀면서도 이게 맞나싶음. 개인적으로 문제를 크게 보지 못하고 사소한 부분을 신경쓰며 코드를 짜다보니 난잡해지고 풀수록 어려워지는 것 같음. 문제는 이것도 나름 추상화랍시고 두 함수로 나눠서 한 것 ㅠ;;
아직은 경험부족이라 생각하고 문제 유형들을 익히는 과정이라 생각해야할 듯함.

난이도 : 실버 2
걸린 시간 : 약 2시간 30분
'''
