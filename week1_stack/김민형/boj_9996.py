n = int(input())
pattern = input().split('*')
length = len(pattern[0]) + len(pattern[1])

for _ in range(n):
    line = input()
    if length > len(line):
        print('NE')  #pattern이 입력 line 보다 길면 프로그램이 동작할 이유가 없다.
    else:
        if pattern[0] == line[:len(pattern[0])] and pattern[1] == line[-len(pattern[1]):]: #에제는 '*' 양쪽으로 하나의 문자만 있지만 여러 문자인 경우도 고려해야함.
            print('DA')
        else:
            print('NE')
