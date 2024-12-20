class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        
    def insert(self, val):
        if val < self.value:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
    
    def find(self, val):
        if val < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(val)
        
        elif val > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(val)
        
        else:
            return self 
tree = TreeNode(5)
tree.insert(11)
tree.insert(3)
tree.insert(9)
tree.insert(2)
tree.insert(8)
tree.insert(7)
tree.insert(9)

print(tree.find(3))