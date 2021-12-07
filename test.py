def search(self, value):
    current = self.root # Start from the root
    if current == None: # Empty tree
        return False 
    if value < current.value:
        current = current.left
    elif value > current.value:
        current = current.right
    else: # element matches current.value
        return True # Element is found