#1001번 - 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

a, b = input("정수를 두개 입력해주세요:").split()

a = int(a)
b = int(b)

print(a-b)

#input을 사용하여 받은 값은 문자열에 여겨진다.
#split() 함수는 특정란 문자로 자를 때 사용하며 공백을 기준으로 입력한 문자열을 공백을 기준으로 잘라 a,b에 각각 대입한다.
#a와 b를 각각 문자열을 int() 함수를 사용하여 정수형으로 변환한다.
#"정수 - 정수" 연산을 수행한다.

#한번에 두개의 값을 입력 받는 경우 split() 함수를 사용하기도 한다.