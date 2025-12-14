
class TNode:         #트리 노드 클래스
    def __init__(self, val):
        self.value = val    #노드가 저장하는 값
        self.left = None  #왼쪽 자식 노드 연결
        self.right = None #오른쪽 자식 노드 연결

# 이진 탐색 트리 삽입 함수
def insert(root, key):
    if root is None:
        return TNode(key)

    if key < root.value:
        root.left = insert(root.left, key)
    elif key > root.value:
        root.right = insert(root.right, key)

    return root

# 서브트리에서 가장 작은 값을 찾는 함수 (후임자를 찾을 때 사용)
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# 이진 탐색 트리 노드 삭제 함수
def delete_node(root, key):
    # 기본 조건: 루트가 비어 있으면 아무 것도 하지 않음
    if root is None:
        return root

    # 삭제할 값을 찾기 위해 왼쪽 또는 오른쪽 서브트리로 이동
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # 삭제할 노드를 찾음
        # 자식이 없는 경우
        if root.left is None and root.right is None:
            return None

        # 자식이 하나만 있는 경우
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # 자식이 두 개 있는 경우
        # 오른쪽 서브트리에서 가장 작은 값을 찾고, 그 값을 현재 노드로 대체
        temp = find_min(root.right)
        root.value = temp.value

        # 후임자를 오른쪽 서브트리에서 삭제
        root.right = delete_node(root.right, temp.value)

    return root

# 삭제 과정 거친 후에 이진 탐색 트리의 성질을 그대로 유지한 상태가 되었는지 확인.
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=' ' )
        inorder_traversal(root.right)

list = [25, 16, 40, 9, 5, 10, 20, 22, 27, 51]

# 사용 예시
root = None
for i in list:
    root = insert(root, i)

print("삭제 전 트리 (중위 순회):")
inorder_traversal(root)
print("\n")

# 노드 삭제
root = delete_node(root, 10)

print("10 을 삭제한 후 트리 (중위 순회):")
inorder_traversal(root)
