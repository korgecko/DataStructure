class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node('숙영')
node2 = Node('지수')
node1.next = node2
head = node1
print(node1.data, '=>', node2.data, '=>', node2.next)
