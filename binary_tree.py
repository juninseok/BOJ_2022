# 이진트리 구현하기

class Node:                             # 노드를 나타내는 class를 생성한다.
    def __init__(self,data):            # 노드를 생성할 때 초기값을 정의해준다.
        self.left = None                # 왼쪽과 오른쪽 자식들을 none으로 설정하고
        self.right = None               # 받은 data를 self를 사용하여 나타냈다.
        self.data = data

class Tree:                             # 트리를 생성하는 class를 생성한다.
    def __init__(self):
        self.root = None                # 가장 부모 노드인 루트노드를 none으로 한 트리를 생성한다.

    def fprint(self,node):              # 전위순회를 하는 함수를 생성한다.
        if node != None:                # node가 none이 어니라면 그 node의 값을 출력한다.
            print(node)
            if node.left != None:       # 노드의 왼쪽 자식이 none이 아니라면 왼쪽 자식을 계속 탐색한다.
                self.fprint(node.left)
            if node.right != None:      # 왼쪽 자식 탐색이 끝난 뒤에 오른쪽 자식들을 탐색한다.
                self.fprint(node.right)


node1 = Node(1)                         # 노드 class를 이용하여 node 객체를 만든다.
node2 = Node(2)                         # 괄호 내부의 값이 data로 들어간다.
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

tree = Tree()                           # 트리 class를 이용하여 tree 객체를 만든디.

tree.root = node1                       # 트리의 루트 노드를 node1로 지정하여 tree.root에 none 대신 다른 값을 할당함.
node1.left = node2                      # 노드 1의 왼쪽 자식을 node2로 설정함.
node1.right = node3                     # 노드 1의 오른쪽 자식을 node3으로 설정함.
node2.left = node4                      # 노드 2의 왼쪽 자식으로 node4를 설정함.
node2.right = node5                     # 노드 2의 오른쪽 자식으로 node5를 설정함.
node3.left = node6                      # 노드 3의 왼쪽 자식으로 node6을 설정함.
node3.right = node7                     # 노드 3의 오른쪽 자식으로 node7을 설정함.

