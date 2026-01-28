class TreeNode:
    def __init__(self,x:int) -> None:
        self.val = x
        self.left = None
        self.right = None



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)