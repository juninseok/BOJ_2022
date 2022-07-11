#10869번 - 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

a, b = input("두 자연수를 입력하세요: ").split()

a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(a/b)      #print(a//b) -- 정수 나누기 연산
print(a%b)
