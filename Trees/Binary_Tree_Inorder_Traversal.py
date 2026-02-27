# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode):
        result, stack = [], []
        curr = root

        while curr or stack:
            while curr:              # Go left as far as possible
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()       # Process node
            result.append(curr.val)
            curr = curr.right        # Visit right subtree

        return result
