# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        curr_depth_building = 0
        curr_node_building = []
        curr_node_num = 0
        stack = []
        i = 0
        
        for i in range(len(traversal)):
            if traversal[i] == '-':
                curr_depth_building += 1
            else:
                curr_node_building.append(traversal[i])
                if i == len(traversal) - 1 or traversal[i + 1] == '-':
                    curr_node_num = int(''.join(curr_node_building))
                    curr_node_building = []
                    print(str(curr_node_num) + ", " + str(curr_depth_building))
                    if curr_depth_building <= len(stack) - 1:
                        for j in range(len(stack) - curr_depth_building):
                            stack.pop()
                    if stack:
                        if stack[-1].left:
                            stack[-1].right = TreeNode(curr_node_num)
                            stack.append(stack[-1].right)
                        else:
                            stack[-1].left = TreeNode(curr_node_num)
                            stack.append(stack[-1].left)
                    else:
                        stack.append(TreeNode(curr_node_num))
                    curr_depth_building = 0

        
        return stack[0]
