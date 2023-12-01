nodeCount = int(input())
nodes = {}
visited = []

for i in range(nodeCount):
    msg = input().split()
    nodes[msg[0]] = [msg[1], msg[2]]
    visited.append(msg[0])

def preorder(root):
    if root != '.':
        print(root, end='') #root
        preorder(nodes[root][0]) #left
        preorder(nodes[root][1]) #right

def inorder(root):
    if root != '.':
        inorder(nodes[root][0]) #left
        print(root, end='') #root
        inorder(nodes[root][1]) #right
        
def postorder(root):
    if root != '.':
        postorder(nodes[root][0]) #left
        postorder(nodes[root][1]) #right
        print(root, end='') #root

preorder('A')
print()
inorder('A')
print()
postorder('A')