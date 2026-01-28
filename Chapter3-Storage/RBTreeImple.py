class RBTree:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def grandparent(self):
        if self.parent is None:
            return None
        else:
            return self.parent.parent
        

    def sibling(self):
        if self.parent is None:
            return None
        if self.parent.left == self:
            return self.parent.right
        else:
            return self.parent.left
        
    def uncle(self):
        if self.parent is None:
            return None
        else:
            return self.parent.sibling()


       
