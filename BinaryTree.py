class TNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 클래스 밖으로 이동
def preorder(n):
    if n is not None:
        print(n.val, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.val, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.val, end=' ')



root = TNode('A')
B = TNode('B')
C = TNode('C')
root.left = B
root.right = C

D= TNode('D')
E= TNode('E')
B.left = D
B.right = E

F= TNode('F')
G= TNode('G')
C.left = F
C.right = G

H= TNode('H')
I= TNode('I')
D.left = H
D.right = I

print('\n  전위 순회 : ', end=' ')
preorder(root)

print('\n  중위 순회 : ', end=' ')
inorder(root)

print('\n  후위 순회 : ', end=' ')
postorder(root)

root = TNode('77')
B = TNode('51')
C = TNode('97')
root.left = B
root.right = C

D= TNode('36')
E= TNode('65')
B.left = D
B.right = E

F= TNode('82')
G= TNode('99')
C.left = F
C.right = G

H= TNode('14')
I= TNode('39')
D.left = H
D.right = I

print('\n  전위 순회 : ', end=' ')
preorder(root)
print('\n  중위 순회 : ', end=' ')
inorder(root)
print('\n  후위 순회 : ', end=' ')
postorder(root)
