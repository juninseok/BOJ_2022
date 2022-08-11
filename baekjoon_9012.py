#9012번 - 올바른 vps를 판단하는 프로그램을 구성하시오

t = int(input("T에 해당하는 정수를 입력하세요 : "))

for _ in range(t):

    count = 0

    vps = list(input("테스트 데이터를 입력하시오 : "))

    for i in vps:
        if i == "(":
            count += 1
        else:
            count -= 1

        if count < 0:   break

    if count == 0:   print("YES")
    else:   print("NO")