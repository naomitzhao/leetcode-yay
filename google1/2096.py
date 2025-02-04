# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # the two nodes will always share a common parent node.
        # find the path from root to each node
        # eliminate common starting letters (get to common parent node)
        # flip path from source to common parent (convert all to U)

        curr_path = []
        path_to_start = []
        path_to_dest = []

        # in order traversal
        def traverse(curr: TreeNode, curr_path, path_to_start, path_to_dest):
            if curr.left:
                curr_path.append('L')
                path_to_start, path_to_dest = traverse(curr.left, curr_path, path_to_start, path_to_dest)
            if curr.right:
                curr_path.append('R')
                path_to_start, path_to_dest = traverse(curr.right, curr_path, path_to_start, path_to_dest)
            
            if curr.val == startValue:
                path_to_start = curr_path[:]
            if curr.val == destValue:
                path_to_dest = curr_path[:]
            
            if curr_path:
                curr_path.pop()

            return (path_to_start, path_to_dest)
        
        path_to_start, path_to_dest = traverse(root, curr_path, path_to_start, path_to_dest)

        first_unique = 0
        while first_unique < len(path_to_start) and first_unique < len(path_to_dest) and path_to_start[first_unique] == path_to_dest[first_unique]:
            first_unique += 1
        
        res = []
        for i in range(first_unique, len(path_to_start)):
            res.append('U')
        for i in range(first_unique, len(path_to_dest)):
            res.append(path_to_dest[i])

        return ''.join(res)