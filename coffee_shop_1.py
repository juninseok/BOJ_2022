# cafe 클래스를 만들어 여러 지점을 만들고 관리하기

class Cafe:

    branch = 0                  # 클래스 변수를 선언함. 클래스 변수 접근은 "클래스이름.변수이름"의 형태로 함.

    def __init__(self):         # __init__라는 함수를 만들어 객체를 생성할 때 처리할 내용을 작성함.
        Cafe.branch += 1        # 객체가 생성될 때 마다 지점의 수를 증가 시킴.

    def __del__(self):          # __del__라는 함수를 만들어 객체가 소멸될 때 처리할 내용을 작성함.
        Cafe.branch -= 1        # 객체가 소멸될 때 마다 지점의 수를 감소 시킴.


cafe1 = Cafe()                  #객체를 생성함.
cafe2 = Cafe()

print(Cafe.branch)

del cafe1                       #객체를 삭제함.

print(Cafe.branch)

del cafe2

print(Cafe.branch)






