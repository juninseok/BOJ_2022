#8393번 - n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input("n에 해당하는 숫자를 입력하세요: "))

value  = 0

for i in range(0,n+1):
    value += i

print(value)