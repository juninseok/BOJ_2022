#4949번 - 문자열이 균형이 맞는지를 판단하는 프로그램을 구성하시오

while True:

    sentence = input("균형을 판단하고자 하는 문자열을 입력하시오 : ")

    if sentence == ".": break

    stack = []

    a = True

    for i in sentence:

        if i == "[" or i == "(":
            stack.append(i)

        elif i == "]":
            if (len(stack) != 0) and stack[-1] == "[":
                stack.pop()
            else:
                a = False
                break

        elif i == ")":
            if (len(stack) != 0) and stack[-1] == "(":
                stack.pop()
            else:
                a = False

    if (len(stack) == 0) and a: print("yes")
    else: print("no")



