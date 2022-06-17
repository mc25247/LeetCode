'''
Given the root of a binary tree, invert the tree, and return its root.

Ex 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Ex2:
Input: root = [2,1,3]
Output: [2,3,1]

Ex 3:
 Input: root = []
 Output: [2,3,1]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            invert= self.invertTree
            root.left,root.right = invert(root.right), invert(root.left)
            return root
