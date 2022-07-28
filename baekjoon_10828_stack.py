# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오

stack = []

n = int(input("스택의 최대 크기를 입력하시오 : "))           # stack의 최대 크기를 입력받음.

for i in range(n):                                      # stack의 크기만큼 반복을 하도록 함.
    command = list(input("명령을 입력하시오:").split())    # 명령어를 입력받는데 명령과 숫자를 공백을 기준으로 구분하여 리스트의 형태로 저장함.

    if command[0] == "push":                    # 명령어가 push이면 마지막 칸에 삽입하는 연산을 수행함.
        stack.append(command[1])

    elif command[0] == "pop":                   # 명령어가 pop이면 두가지 경우로 나누어 수행함.
        if len(stack) == 0:                     # stack의 길이가 0이면 1을 출력한다.
            print(1)
        else:                                   # stack의 길이가 0이 아니면 가장 마지막에 삽입된 자료를 출력하고 제거한다.
            print(stack[-1])
            del stack[-1]

    elif command[0] == "size":                  # 명령어가 size이면 stack의 길이를 반환함.
        print(len(stack))

    elif command[0] == "empty":                 # 길이를 판별하여 비어있다면 1을 아니라면 0을 출력함.
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    else:                                       # top 명령어를 받아야하는데 else로 일괄적으로 받음.
        if len(stack) == 0:                     # 비어있는 stack의 경우에 -1을 반환하고 아닌 경우 스택의 가장 위에 있는 값을 출력함.
            print(-1)
        else:
            print(stack[-1])

# 스택의 push와 pop 연산을 하며 가장 마지막에 삽입된 자료가 가장 먼저 출력되는 LIFO 구조를 리스트를 사용하여 나타낸 STACK 관련 문제라고 생각함.
