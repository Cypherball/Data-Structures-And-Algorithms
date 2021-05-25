class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return "<Node data=" + str(self.data) + ">"
    
class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
    
    def get_length(self):
        return self.length

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.length += 1
        else:
            node = self.head
            while (node.next):
                node = node.next
            node.next = new_node
            self.length += 1
        return new_node

    def push(self, data):
        return self.append(data)
    
    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1
        return self.head
    
    def insert(self, data, pos=1):
        if pos == 1: return self.prepend(data)
        node = Node(data)
        temp = self.head
        for _ in range(pos - 2):
            if (temp.next): temp = temp.next
            else: return -1
        node.next = temp.next
        temp.next = node
        self.length += 1
        return node

    def pop(self):
        if self.length < 1: return None
        elif self.length == 1:
            node = self.head
            self.head = None
            self.length -= 1
            return node
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        node = temp.next
        temp.next = None
        self.length -= 1
        return node

    def reverse(self):
        if self.length < 2: return
        prev = _next = None
        current = self.head
        while (current):
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        self.head = prev

    def reverse_recursive(self, node=None):
        if not node: node = self.head
        if not node.next:
            self.head = node
            return
        self.reverse_recursive(node.next)
        node.next.next = node
        node.next = None
    
    def print(self, output = 'True'):
        string = ''
        if self.length > 0:  
            node = self.head
            while(1):
                if node.next:
                    string += str(node.data) + ' -> '
                    node = node.next
                else:
                    string += str(node.data)
                    break
        if output: print(string)
        return string
    
    def print_reverse(self, node=None):
        if not node: node = self.head
        if node.next: self.print_reverse(node.next)
        print(str(node.data), end=' ')

    def __repr__(self) -> str:
        return "<LinkedList Nodes=<" + self.print(output=False) + ">>"

ll = LinkedList()
#ll.print()
ll.prepend(2)
ll.append(5)
ll.insert(4,2)
#ll.print()
ll.append("Hello")
ll.append(['world', 1, 'xD'])
ll.prepend(9)
ll.insert(55,5)
ll.pop()
ll.print()
ll.print_reverse()
print()
ll.reverse_recursive()
ll.print()