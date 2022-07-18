#10871번 - 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
n,x = input().split()

n = int(n)
x = int(x)

list_a = []
output = []

list_a += input().split()

for i in range(n):
    if x > int(list_a[i]):
        output.append(list_a[i])

print(*output)
