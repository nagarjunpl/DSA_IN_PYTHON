# Define Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inorder function
def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(1)

print("Inorder Traversal:")
inorder(root)
