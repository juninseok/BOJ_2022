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
