#2588번 - 3자리 숫자간의 곱셈 연산 과정 출력하시오

a = int(input("3자리 숫자를 입력하세요 :"))
b = input("3자리 숫자를 입력하세요 :")

c = a * int(b[2])
d = a * int(b[1])
e = a * int(b[0])

value = e * 100 + d * 10 + c

print(c)
print(d)
print(e)
print(value)





