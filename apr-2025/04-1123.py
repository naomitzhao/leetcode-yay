# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # return greatest height and either left or right or current node
        # based on depths of each tree
        def getLcaNode(curr):
            leftNode, leftHeight = None, 0
            rightNode, rightHeight = None, 0

            if curr.left:
                leftNode, leftHeight = getLcaNode(curr.left)
            if curr.right:
                rightNode, rightHeight = getLcaNode(curr.right)
            
            if leftHeight > rightHeight:
                return leftNode, leftHeight + 1
            if rightHeight > leftHeight:
                return rightNode, rightHeight + 1
            else:
                return curr, leftHeight + 1
        
        return getLcaNode(root)[0]
            