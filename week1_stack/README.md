### stack 1주차 내용

작성자 김건호

## 1) stack이란?
data들을 접시 쌓듯이, 후입 선출 구조로 정보들을 다루기 가능한 구조. <br>
stack은 양 방향으로 정보의 삽입, 삭제, 조회가 이루어지지 않음. <br>
접시를 쌓아둔 구조를 생각하면 편하다. <br>
맨 위의 데이터를 조회 가능하고, <br>
맨 위의 데이터를 삭제 가능하다. <br>
또 추가할 때는, 맨 위부터 추가가 가능함. <br>
만약 중간 부분을 건드리거나, <br>
제일 아랫 부분을 건드린다면 무너질 것이다. <br>
이는 stack의 의미와 멀어진다. <br>

## 2) stack의 ADT
스택이 비어있지 않다면(중요) 스택의 최상단 원소를 조회하는 top() <br>
스택이 비어있지 않다면(중요) 스택의 최상단 원소를 조회 후 제거 가능한 pop() <br>
스택의 용량이 초과되지 않았다면(중요) 스택의 최상단에 새로운 원소를 추가 가능한 push()
스택이 비어있다면 true, 아니라면 false를 반환하는 empty() <br>
스택의 사이즈가 얼마인지 알려주는 size() <br>
배열 기반의 스택의 용량이 다 찼다면 true, 아니라면 false를 반환하는 full() <br> 

## 3) 구현

python : 스택을 따로 제공하지 않고, 만약 사용한다면 dequeue나 list를 사용하거나 class를 사용하여 구현함. <br>
c++ : #include <stack> 이후 사용 가능. <br>
c : linked list의 형태로 구현하거나, 배열 기반의 구조체 사용. <br>


# 3-1) python code 
<br>


class Stack :
    def __init__ (self) :
        self.__stack__=[]
    def top(self) :    
        try :
            return self.stack[-1]
        except Exception as e:    
                print("stack's size zero. Try push!", e)
    def pop(self) :
        try :
            return self.stack[-1]
        except Exception as e:    
                print("stack's size zero. Try push!", e)      
    def push(self, data) : 
        (self.__stack__).append(data)
    def empty(self) :
        if len(self.__stack__) == 0 :
            return True
        else :
            return False
    def size(self) :
        return len(self.__stack__)        
    
        
    
            
    
    
    
    
    
