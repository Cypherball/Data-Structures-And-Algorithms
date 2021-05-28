class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = self.right = None

# Uses global variable 'prev' to keep track of previously visited node
prev = None

def is_BST(root) -> bool:
    global prev
    prev = None
    return is_BST_Util(root)

def is_BST_Util(root, isRightChild = False) -> bool:
    global prev
    if not root: return True
    if not is_BST_Util(root.left): return False
    if prev != None:
        if isRightChild:
            # right child can only be greater than root
            if root.data <= prev.data: return False
        else:
            # root can be greater than or equal to left child
            if root.data < prev.data: return False
    prev = root
    return is_BST_Util(root.right, True)


# root = Node(3)
# root.left = Node(2)
# root.right = Node(5)
# root.left.left = Node(1)
# root.right.left = Node(4)
# root.right.left.left = Node(40)

root = Node(50)
root.left = Node(30)
root.right = Node(90)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(70)
root.left.left.left = Node(9)
root.left.right.right = Node(50)
root.right.left.left = Node(60)
root.right.left.right = Node(80)
    
if (is_BST(root)):
    print("Is BST")
else:
    print("Not a BST")