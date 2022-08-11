#1406번 - 커서를 이용한 에디터 관련 프로그램을 구현하시오

sentence = list(input("편집기에 입력할 문자열을 입력하시오 : "))
order_num = int(input("입력할 명령어의 개수를 입력하시오 : "))

cursor = len(sentence)

for _ in range(order_num):

    order = input("명령어를 입력하세요 : ").split()

    if order[0] == "L":
        if cursor <= 0:
            continue
        else:
            cursor -= 1
        print(cursor)

    elif order[0] == "D":
        if cursor > len(sentence):
            continue
        else:
            cursor += 1

    elif order[0] == "B":
        if cursor == 0:
            continue
        else:
            cursor -= 1
            sentence.pop(cursor)

    else:
        sentence.insert(cursor,order[1])
        cursor += 1

for i in sentence:
    print(i, end="")
