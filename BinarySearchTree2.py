class TNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def search(currentNode, key):
    if currentNode == None:
        return False
    elif key == currentNode.value:
        return currentNode
    elif key < currentNode.value:
        return search(currentNode.left, key)
    else:
        return search(currentNode.right, key)

def insert(root, key):
    if root is None:
        return TNode(key) # None 을 만나면 새로운 노드를 반환
    if key < root.value:
        root.left = insert(root.left, key)
    elif key > root.value:
        root.right = insert(root.right, key)
    return root

import random

fifty_random_numbers = [random.randint(0, 100) for i in range(50)]
print(fifty_random_numbers)

# 이진 탐색 트리 생성 및 사용 예.
root = None
for i in fifty_random_numbers:
    root = insert(root, i)
key = random.randint(1, 100)
print('key', key)
result = search(root, key)
if result:
    print(f"노드 {result.value}를 찾았습니다.")
else:
    print(f"노드를 찾지 못했습니다.")
