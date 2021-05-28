class BSTNode:
    def __init__(self, data = None) -> None:
        self.data = data
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self, data=None) -> None:
        if data: self.root = BSTNode(data)
        else: self.root = None

    def get_root(self):
        return self.root

    def search(self, root, data):
        if root is None or root.data == data: return root
        if data <= root.data:
            return self.search(root.left, data)
        return self.search(root.right, data)

    def insert(self, root, data, allow_duplicates=True):
        if not root:
            node = BSTNode(data)
            if not self.root: self.root = node
            return node
        if not allow_duplicates and data == root.data:
            # prevent addition of duplicate data nodes
            return root
        if data <= root.data:
            root.left = self.insert(root.left, data, allow_duplicates)
        else: root.right = self.insert(root.right, data, allow_duplicates)
        return root
    
    # DEPTH FIRST SEARCH TRAVERSALS

    def print_inorder(self, root):
        if not root: return None
        self.print_inorder(root.left)
        print(root.data, end=' ')
        self.print_inorder(root.right)
    
    def print_preorder(self, root):
        if not root: return
        print(root.data, end=' ')
        self.print_preorder(root.left)
        self.print_preorder(root.right)
    
    def print_postorder(self, root):
        if not root: return
        self.print_postorder(root.left)
        self.print_postorder(root.right)
        print(root.data, end=' ')

    # -------------------------------

    # BREADTH FIRST SEARCH TRAVERSAL (Level-Order)
    def print_bfs(self):
        if not self.root: return None
        q = []
        q.append(self.root)
        while(len(q) > 0):
            node = q.pop(0)
            print(node.data, end=' ')
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    # -------------------------------

    def print_left_view(self):
        if not self.root: return None
        q = []
        q.append(self.root)
        while(len(q) > 0):
            for i in range(len(q)):
                node = q.pop(0)
                if i == 0: print(node.data, end=' ')
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
    
    def print_right_view(self):
        if not self.root: return None
        q = []
        q.append(self.root)
        while(len(q) > 0):
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if i == n-1: print(node.data, end=' ')
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

    def find_min(self, root):
        if not root: return None
        if root.left == None: return root.data
        return self.find_min(root.left)
        
    def find_max(self, root):
        if not root: return None
        if root.right == None: return root.data
        return self.find_max(root.right)

    def get_height(self, root):
        # counting number of nodes in longest path from root to leaf node
        if not root: return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1


# Tests
bst = BinarySearchTree(50)
bst.insert(bst.get_root(), 30)
bst.insert(bst.get_root(), 20)
bst.insert(bst.get_root(), 40)
bst.insert(bst.get_root(), 90)
bst.insert(bst.get_root(), 70)
bst.insert(bst.get_root(), 60)
bst.insert(bst.get_root(), 80)
bst.insert(bst.get_root(), 80, False) # won't insert duplicate
bst.insert(bst.get_root(), 50)
bst.insert(bst.get_root(), 9)

print('Inorder:')
inorder = bst.print_inorder(bst.get_root())
print()

print('\nPreorder:')
bst.print_preorder(bst.get_root())
print()

print('\nPostorder:')
bst.print_postorder(bst.get_root())
print()

print('\nLevel order:')
bst.print_bfs()
print()

print('\nLeft View:')
bst.print_left_view()
print('\n')

print('\nRight View:')
bst.print_right_view()
print('\n')

print("MIN:", bst.find_min(bst.get_root()))
print("MAX:", bst.find_max(bst.get_root()))

print("HEIGHT:", bst.get_height(bst.get_root()))
