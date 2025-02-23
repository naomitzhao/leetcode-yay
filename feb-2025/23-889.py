# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.preIdx = 0
        self.postIdx = 0
        
        def construct():
            root = TreeNode(preorder[self.preIdx])
            self.preIdx += 1
            
            if root.val != postorder[self.postIdx]:
                root.left = construct()
            
            if root.val != postorder[self.postIdx]:
                root.right = construct()
            
            self.postIdx += 1
            return root
        
        return construct()
