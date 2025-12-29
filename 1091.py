class Node:
    def __init__(self, value) -> None:
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
        self.count = 1
    
    def has_children(self):
        return self.left != None or self.right != None
    
    def add(self, val):

        if val == None:
            return
        if val == self.value:
            self.count += 1
            return
        if not self.has_children():
            node = Node(val)
            node.parent = self
            if val < self.value:
                self.left = node
            else:
                self.right = node
            return
        
        if val < self.value:
            if self.left == None:
                node = Node(val)
                node.parent = self
                self.left = node
            else:
                self.left.add(val)
        else:
            if self.right == None:
                node = Node(val)
                node.parent = self
                self.right = node
            else:
                self.right.add(val)

    def _find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def remove(self, val):
        # Finding the right one
        if val < self.value:
            if self.left:
                self.left.remove(val)
            return
        elif val > self.value:
            if self.right:
                self.right.remove(val)
            return
        
        if self.count > 1:
            # several occurrences
            self.count -= 1
            return

        # Case 1 : No children
        if not self.left and not self.right:
            if self.parent:
                if self.parent.left == self:
                    self.parent.left = None
                else:
                    self.parent.right = None
            else:
                self.value = None
                self.count = 0
            return

        # Case 2 : A single one
        if self.left and not self.right:
            if self.parent:
                if self.parent.left == self:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
            self.left.parent = self.parent
            return

        if self.right and not self.left:
            if self.parent:
                if self.parent.left == self:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
            self.right.parent = self.parent
            return

        # Case 3 : 2 children
        successor = self.right._find_min()
        self.value = successor.value
        self.count = successor.count
        successor.count = 1  # avoid infinite loop
        successor.remove(successor.value)
    
    def print_node(self):
        if self.left:
            self.left.print_node()
        for i in range(self.count):
            print(self.value, end=" ")
        if self.right:
            self.right.print_node()

n = int(input())
head = None
for i in range(n):
    a, b = input().split()
    b = int(b)
    if a == "add":
        if not head:
            head = Node(b)
        else:
            head.add(b)
    else:
        if head:
            head.remove(b)
    
    head.print_node()
    print()