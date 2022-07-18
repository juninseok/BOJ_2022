#2438번 - 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

N = int(input("N에 해당할 정수를 입력하세요:"))

for i in range(N):
    print("*" * (i+1))


#이중 for문을 이용하는 방법

'''output = ""
for i in range(1,N+1):
    for j in range(i):
        output += "*"
    output += "\n"

print(output)'''