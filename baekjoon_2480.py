#2480번 - 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

a,b,c = input("주사위 3개의 눈을 입력하세요: ").split()

a = int(a)
b = int(b)
c = int(c)

if a == b == c:
    print(10000 + (a*1000))

elif a == b != c or a == c != b:
    print (1000 + (a*100))

elif b == c != a:
    print(1000 + (b*100))

else:
    if a > b and a > c:
        print(a * 100)
    elif b > a and b > c:
        print(b * 100)
    else:
        print(c * 100)


