import bst 

class Derived_BST(bst.BST):
    def __init__(self):
        super().__init__()

    def is_leaf(self, node):
        if node.left == None and node.right == None:
            return True
        else:
            return False

    def find_node(self, value):
        current = self.root
        while current != None:
            if current.value == value:
                return current
            if current.value < value:
                current = current.right
            else:
                current = current.left
        return None

    def is_branch(self, node):
        return self.is_leaf(node) == False

    def parent_node(self, value):
        parent = None
        current = self.root
        while current != None:
            if current.value == value:
                return parent.value
            if current.value < value:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left
        return None

 
    def total_leaf_nodes(self, node):
        if node == None:
            return 0
        if self.is_leaf(node):
            return 1
        else:
            return self.total_leaf_nodes(node.left) + self.total_leaf_nodes(node.right)

    def total_leaf_nodes_iterative(self, node):
        if node == None:
            return 0
        queue = []
        queue.append(node)
        count = 0
        while len(queue) > 0:
            current = queue.pop(0)
            if self.is_leaf(current):
                count += 1
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        return count

    def total_nonleaf_nodes(self):
        return self.size - self.total_leaf_nodes(self.root)
        
    def get_max(self):
        current = self.root
        while current.right != None:
            current = current.right
        return current.value

    def get_min(self):
        current = self.root
        while current.left != None:
            current = current.left
        return current.value

    def breadth_first(self):
        #print out level by level
        if self.root == None:
            return None
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.value, end = ' ')
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
            