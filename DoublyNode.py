class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

node1 = DoublyNode(10)
node2 = DoublyNode(20)

# 노드 연결
node1.next = node2
node2.prev = node1

# 연결 확인 출력
print("=== 정방향 탐색 ===")
print(f"node1.data: {node1.data}")
print(f"node1.next.data: {node1.next.data}")

print("\n=== 역방향 탐색 ===")
print(f"node2.data: {node2.data}")
print(f"node2.prev.data: {node2.prev.data}")

print("\n=== 연결 구조 ===")
print(f"{node1.data} <-> {node2.data}")
