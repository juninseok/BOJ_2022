# stack 구현하기

class Stack:
    def __init__(self):                 #리스트를 이용하여 stack을 나타냄.
        self.stack = []

    def empty(self):                    #비어있는 stack인지 확인하는 함수
        if len(self.stack) == 0:
            return True
        return False

    def push(self, data):               #data를 삽입하는 push 함수
        self.stack.append(data)

    def pop(self):                      #data를 꺼내는 pop 함수
        if self.empty():
            return "비어있는 스택입니다."
        else:
            return self.stack.pop()

    def top(self):                      #top값을 나타내는 함수
        if self.empty():
            return "비어있는 스택입니다."
        else:
            return self.stack[-1]       #가장 마지막을 나타냄 --> index -1을 이용함.
