class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        self.parent = [-1] * n
        self.depth = [0] * n

        component_cost = [-1] * n

        for edge in edges:
            self._union(edge[0], edge[1])
        
        for edge in edges:
            root = self._find(edge[0])
            component_cost[root] &= edge[2]
        
        ans = []
        for start, end in query:
            startFind = self._find(start)
            if startFind != self._find(end):
                ans.append(-1)
            else:
                root = startFind
                ans.append(component_cost[root])
        
        return ans

    def _find(self, node):
        # node is its own parent
        if self.parent[node] == -1:
            return node
        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]
    
    def _union(self, node1, node2):
        root1 = self._find(node1)
        root2 = self._find(node2)

        # already in same component
        if root1 == root2:
            return
        
        # make root of deeper tree become parent
        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1
        
        self.parent[root2] = root1

        if self.depth[root1] == self.depth[root2]:
            self.depth[root1] += 1
            
