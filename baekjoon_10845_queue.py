#10845번 - 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

queue = []

n = int(input("큐의 최대 크기를 입력하시오 : "))

for i in range(n):
    command = list(input("명령어를 입력해주세요 :").split())

    if command[0] == "push":                    # 명령어가 push이면 마지막 칸에 삽입하는 연산을 수행함.
        queue.append(command[1])

    elif command[0] == "pop":                   # 명령어가 pop이면 두가지 경우로 나누어 수행함.
        if len(queue) == 0:                     # queue의 길이가 0이면 1을 출력한다.
            print(-1)
        else:                                   # queue의 길이가 0이 아니면 가장 처음에 삽입된 자료를 출력하고 제거한다.
            print(queue[0])
            del queue[0]

    elif command[0] == "size":                  # 명령어가 size이면 queue의 길이를 반환함.
        print(len(queue))

    elif command[0] == "empty":                 # 길이를 판별하여 비어있다면 1을 아니라면 0을 출력함.
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":                 # 명령어가 front인 경우, 가장 앞에 있는 자료를 반환함.
        if len(queue) == 0:                     # 비어있는 queue의 경우에 -1을 반환함.
            print(-1)
        else:
            print(queue[0])

    else:                                       # 명령어가 back인 경우를 else문으로 받음.
        if len(queue) == 0:                     # 비어있는 queue의 경우에 -1을 반환하고 아닌 경우 queue의 가장 늦게 삽입된 값을 출력함.
            print(-1)
        else:
            print(queue[-1])

# 큐의 push와 pop 연산을 수행하고 front와 back을 통해 해당하는 값을 출력하도록 함.
# 큐의 가장 먼저 들어온 것이 가장 먼저 출력되는 FIFO 구조를 리스트를 이용하여 구현함.