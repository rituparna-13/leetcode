# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# Time complexity: O(h) given h = height of the tree
# Space complexity: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # case 1: check right subtree if p and q values are greater than current node
            if root.val < p.val and root.val < q.val:
                root = root.right
            # case 2: check left subtree if p and q values are less than current node
            elif root.val > p.val and root.val > q.val:
                root = root.left
            # case 3: return current node if either p or q = root.val
            else:
                return root
        return None
        
